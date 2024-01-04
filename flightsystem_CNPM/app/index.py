from flask import Flask, render_template, request, redirect, url_for, jsonify, send_file, Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, FlightDetail, Customer, Admin, ConfirmationToken, Schedule
from flask_mail import Mail, Message
import uuid
from flask_mysqldb import MySQL
from datetime import datetime
import requests
import qrcode
from flask_admin import Admin, expose
flightapp = Flask(__name__)



# SQLAlchemy configuration
#flightapp.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:ledung123.vn@localhost/labsaledb?charset=utf8mb4'




# Duong dan den trang chu
@flightapp.route("/")
def home():

    return render_template("home.html")

# Duong dan den trang dang nhap
@flightapp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@flightapp.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if the entered credentials match a Customer
        customer = Customer.query.filter_by(email=email).first()
        if customer and check_password_hash(customer.password, password):
            # Log in the customer
            return redirect(url_for('home'))

        # Check if the entered credentials match an Admin
        #admin = Admin.query.filter_by(email=email).first()
       #if admin and check_password_hash(admin.password, password):
            # Log in the admin
          #  return redirect(url_for('dashboard'))

        return render_template('login.html', message='Invalid email or password.')

    return render_template('login.html', message='')

# Duong dan den trang dat ve
@flightapp.route("/booktickets")
def booktickets():
    return render_template("booktickets.html")

# Duong dan den trang ban ve
@flightapp.route("/sellticket", methods=["GET", "POST"])
def sellticket():
    if request.method == "POST":
        # Process the form data here
        # For example, you can access form values using request.form['fieldname']
        # Implement your logic for selling tickets

        # Redirect to a success page or home page after form submission
        return redirect(url_for('home'))

    # Render the sellticket.html template
    return render_template("sellticket.html")

@flightapp.route("/ScheduleManagement")
def ScheduleManagement():

    # Pass the data to the template
    return render_template("ScheduleManagement.html")

@flightapp.route("/flightManagement")
def flightManagement():

        return render_template("flightManagement.html")

@flightapp.route("/thanhToan", methods=['GET', 'POST'])
def thanhToan():
    if request.method == 'POST':
        return render_template('thanhToan.html')


@flightapp.route("/reportRevenue")
def reportRevenue():
    return render_template("reportRevenue.html")

@flightapp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Lấy thông tin từ form
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        address = request.form.get('address')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # Kiểm tra các trường thông tin
        if not name or not email or not phone or not address or not password or not confirm_password:
            return render_template('register.html', message='Vui lòng điền đầy đủ thông tin.')

        # Kiểm tra xác nhận mật khẩu
        if password != confirm_password:
            return render_template('register.html', message='Mật khẩu và xác nhận mật khẩu không khớp.')

        # Kiểm tra email đã tồn tại hay chưa (thực tế, bạn cần kiểm tra cả các trường khác nếu muốn)
        if Customer.query.filter_by(email=email).first():
            return render_template('register.html', message='Email đã tồn tại. Vui lòng chọn email khác.')

        # Hash mật khẩu trước khi lưu vào cơ sở dữ liệu
        hashed_password = generate_password_hash(password, method='sha256')

        # Nếu kiểm tra qua tất cả các điều kiện, thực hiện lưu thông tin vào cơ sở dữ liệu
        # (code thêm thông tin vào cơ sở dữ liệu ở đây)

        # Lưu thông tin vào cơ sở dữ liệu, bao gồm cả hashed_password
        new_customer = Customer(
            name=name,
            email=email,
            phone=phone,
            address=address,
            password=hashed_password
        )
        db.session.add(new_customer)
        db.session.commit()

        # Tạo token xác nhận và lưu vào cơ sở dữ liệu
        confirmation_token = generate_confirmation_token()
        save_confirmation_token(email, confirmation_token)

        # Gửi email xác nhận
        send_confirmation_email(email, confirmation_token)

        # Chuyển hướng hoặc hiển thị thông báo thành công
        return redirect(url_for('login'))

    # Nếu là GET request, hiển thị trang đăng ký
    return render_template('register.html', message='')

# Route xác nhận từ email
@flightapp.route('/confirm/<token>')
def confirm_email(token):
    email = confirm_email_token(token)
    if email:
        # Xác nhận tài khoản trong cơ sở dữ liệu
        confirm_user(email)
        return render_template('confirmation_success.html', email=email)
    else:
        return render_template('confirmation_fail.html')

# Endpoint for generating VNPAY QR code
@flightapp.route("/generate_qr_code", methods=['POST'])
def generate_qr_code():
    if request.method == 'POST':
        # Process input data and build URL for payment
        form = request.form  # Update with the actual form object
        order_type = form.get('order_type', '')
        order_id = form.get('order_id', '')

        # Check if amount is provided and not empty
        amount_str = form.get('amount', '')
        amount = float(amount_str) if amount_str else 0.0  # Set a default value if empty

        # Check if order_desc is provided and not empty
        order_desc = form.get('order_desc', '')
        bank_code = form.get('bank_code', '')
        language = form.get('language', '')
        ipaddr = request.remote_addr

        # Build URL Payment
        vnp_request_data = {
            'vnp_Version': '2.1.0',
            'vnp_Command': 'pay',
            'vnp_TmnCode': 'YOUR_MERCHANT_CODE',  # Replace with your actual merchant code
            'vnp_Amount': int(amount * 100),  # Convert to cents
            'vnp_CurrCode': 'VND',
            'vnp_TxnRef': order_id,
            'vnp_OrderInfo': order_desc,
            'vnp_OrderType': order_type,
            'vnp_Locale': language if language and language != '' else 'vn',
            'vnp_CreateDate': datetime.now().strftime('%Y%m%d%H%M%S'),
            'vnp_IpAddr': ipaddr,
            'vnp_ReturnUrl': url_for('payment_success', _external=True),
        }

        # Check bank_code, if bank_code is not empty, include it in the request
        if bank_code and bank_code != "":
            vnp_request_data['vnp_BankCode'] = bank_code

        # Use your VNPAY API integration logic to generate the payment URL
        vnpay_payment_url = generate_vnpay_payment_url(vnp_request_data)
        print(vnpay_payment_url)

        # Redirect to VNPAY
        return redirect(vnpay_payment_url)

    else:
        return redirect(url_for('home'))

# Endpoint to handle payment success
@flightapp.route("/payment_success")
def payment_success():
    # Handle successful payment here
    # You can retrieve additional details from the VNPAY response if needed
    # Update your database or perform any other necessary actions

    return render_template('payment_success.html')

@flightapp.route("/loginadmin")

def loginadmin():
    return render_template('loginadmin.html')
@flightapp.route('/generate_qr')
def generate_qr():
    data_to_encode = "Hello, this is your QR code data!"

    # Tạo mã QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data_to_encode)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Lưu ảnh QR vào một tệp (hoặc có thể trả về trực tiếp nếu muốn)
    img.save("static/qrcode.png")

    # Chuyển hướng đến trang mới (qr_page)
    return redirect(url_for('qr_page'))

@flightapp.route("/qr_page")
def qr_page():
    return render_template('qr_page.html')

def generate_vnpay_payment_url(request_data):
    # Build the VNPAY payment URL using the provided data
    vnpay_api_url = 'https://sandbox.vnpayment.vn/paymentv2/vpcpay.html'

    # Create the complete URL with query parameters
    payment_url = f"{vnpay_api_url}?{'&'.join(f'{key}={value}' for key, value in request_data.items())}"

    return payment_url


def generate_vnpay_payment_url(request_data):
    # This is a placeholder; implement your logic to interact with VNPAY API and get the payment URL
    # You may need to use the `requests` library to send a request to the VNPAY API endpoint
    # and extract the payment URL from the response.

    # Example:
    vnpay_api_url = 'https://sandbox.vnpayment.vn/paymentv2/vpcpay.html'
    response = requests.get(vnpay_api_url, params=request_data)

    # Extract the payment URL from the response
    payment_url = response.url

    return payment_url
# Các hàm hỗ trợ
def generate_confirmation_token():
    # Tạo token xác nhận, sử dụng UUID
    return str(uuid.uuid4())

def save_confirmation_token(email, token):
    # Lưu token vào cơ sở dữ liệu
    confirmation_token = ConfirmationToken(email=email, token=token)
    db.session.add(confirmation_token)
    db.session.commit()

def send_confirmation_email(email, token):
    # Gửi email xác nhận
    subject = "Xác nhận đăng ký"
    confirm_url = url_for('confirm_email', token=token, _external=True)
    body = render_template('confirmation_email.html', confirm_url=confirm_url)

    # Use Flask-Mail to send the email
    msg = Message(subject, recipients=[email], body=body)

def confirm_email_token(token):
    # Kiểm tra token xác nhận và trả về email nếu hợp lệ
    confirmation_token = ConfirmationToken.query.filter_by(token=token).first()
    return confirmation_token.email if confirmation_token else None

def confirm_user(email):
    # Đánh dấu tài khoản người dùng là đã xác nhận
    user = Customer.query.filter_by(email=email).first()
    if user:
        user.confirmed = True
        db.session.commit()

if __name__ == '__main__':
    flightapp.run(debug=True)