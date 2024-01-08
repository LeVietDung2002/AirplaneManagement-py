// auth.js

const data = {
  "roles": [
    {"id": 1, "name": "admin"},
    {"id": 2, "name": "user"}
  ],
  "users": [
    {"id": 1, "username": "admin", "email": "admin@example.com", "password": "admin_pass", "role_id": 1},
    {"id": 2, "username": "user1", "email": "user1@example.com", "password": "user1_pass", "role_id": 2},
    {"id": 3, "username": "user2", "email": "user2@example.com", "password": "user2_pass", "role_id": 2}
  ],
  "admins": [
    {"id": 1, "role_id": 1}
  ],
  "customers": [
    {"customerID": "C1", "name": "John Doe", "email": "john@example.com", "phone": "123-456-7890", "address": "123 Main St"}
  ],
  "logins": [
    {"id": 1, "username": "admin", "password": "admin_pass", "user_id": 1}
  ],
  "confirmation_tokens": [
    {"id": 1, "user_id": 2, "token": "abc123"}
  ],
  "employees": [
    {"employeeID": "E1", "name": "Employee 1", "email": "employee1@example.com", "phone": "987-654-3210", "position": "Manager", "login_id": 1}
  ]
};

const rolesData = data.roles || [];
const usersData = data.users || [];
const adminsData = data.admins || [];
const customersData = data.customers || [];
const loginsData = data.logins || [];
const confirmationTokensData = data.confirmation_tokens || [];
const employeesData = data.employees || [];

// Function to authenticate user
async function authenticateUser(username, password) {
  const user = usersData.find(
    (u) => u.username === username && u.password === password
  );

  if (user) {
    return user;
  } else {
    return null;
  }
}

// Function to check user roles
async function checkUserRole(userId) {
  const user = usersData.find((u) => u.id === userId);
  const role = rolesData.find((r) => r.id === user.role_id);

  if (role) {
    return role.name;
  } else {
    return null;
  }
}

// Example usage
console.log("Roles Data:", rolesData);
console.log("Users Data:", usersData);
console.log("Admins Data:", adminsData);
console.log("Customers Data:", customersData);
console.log("Logins Data:", loginsData);
console.log("Confirmation Tokens Data:", confirmationTokensData);
console.log("Employees Data:", employeesData);
