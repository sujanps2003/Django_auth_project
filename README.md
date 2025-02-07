# Django Authentication System

This is a Django-based user authentication system that includes:

- User registration with username and email validation.
- User login and logout functionality.
- Forgot password and reset password features.
- Change password for authenticated users.
- A user dashboard and profile page.

## Features

✅ User authentication with **username/email** and password. ✅ **Signup page** with validation (max length, unique username, strong password). ✅ **Login page** with username/email and password. ✅ **Forgot password functionality** (uses Django console backend to print reset link). ✅ **Change password feature** (requires authentication). ✅ **Dashboard & Profile page** (only accessible after login). ✅ Restricts access to certain pages based on authentication. ✅ Uses **Django's built-in authentication system** and template inheritance.

## Installation

### Clone the Repository

```sh
git clone https://github.com/sujanps2003/Django_auth_project.git
cd django_auth
```

### Create a Virtual Environment

```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### Install Dependencies

```sh
pip install django
```

### Run Database Migrations

```sh
python manage.py migrate
```

### 5️⃣ Create a Superuser (Optional)

```sh
python manage.py createsuperuser
```

### 6️⃣ Run the Development Server

```sh
python manage.py runserver
```

## Configuration

### 🔹 Settings for Email (Uses Console Backend)

To handle password reset emails, **Django prints the reset link to the console** instead of sending real emails.

In `settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

This will print the password reset link to the console.

## URL Patterns

| URL                        | Functionality                              |
| -------------------------- | ------------------------------------------ |
| `/login/`                  | Login Page                                 |
| `/signup/`                 | User Registration Page                     |
| `/dashboard/`              | User Dashboard (Authenticated users only)  |
| `/profile/`                | Profile Page (Displays user details)       |
| `/logout/`                 | Logout User                                |
| `/forgot-password/`        | Request password reset email               |
| `/reset/<uidb64>/<token>/` | Reset password page                        |
| `/change-password/`        | Change password (Authenticated users only) |

## How It Works

### 🔹 User Registration

- Users can **sign up** using their **email and username**.
- Password validation ensures a **minimum of 8 characters**.
- If the user already exists, an error message is displayed.
- After registration, the user is redirected to the **login page**.

### 🔹 Login & Authentication

- Users can log in with **either username or email**.
- If the credentials are incorrect, an error message is shown.
- Upon successful login, the user is redirected to the **dashboard**.

### 🔹 Forgot Password & Reset Password

- The **Forgot Password** page allows users to reset their password.
- Django **prints the reset link** in the console instead of sending an email.
- The user can set a **new password** using the reset link.

### 🔹 Change Password

- Users must be **logged in** to change their password.
- The old password is required for verification.
- After changing the password, the user is redirected to the **dashboard**.

### 🔹 Dashboard & Profile

- The **dashboard** shows a welcome message with the username.
- The **profile page** displays user details (username, email, date joined).
- Both pages are accessible **only after logging in**.

## Contributing

Feel free to **fork** this repository and submit pull requests. 😊

## License

This project is open-source and available under the **MIT License**.

---

✨ **Built with Django 5.0.6** ✨
