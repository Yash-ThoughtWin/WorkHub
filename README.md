# WorkHUB — Team Collaboration Platform

WorkHUB is a backend Team Collaboration Platform built with FastAPI. It enables organizations to manage users, projects, tasks, comments, documents, search, dashboards, and audit logs through secure REST APIs.

# Tech Stack

**Language:**          Python
**Framework:**         FastAPI
**Database:**          PostgreSQL
**ORM:**               SQLAlchemy
**Migrations:**        Alembic
**Validation:**        Pydantic
**Authentication:**    JWT
**Password Security:** Password Hashing
**Testing:**           Pytest
**Containerization:**  Docker
**Version Control:**   Git
---

## User Roles
# Admin
* Manage users and roles
* Manage projects and tasks
* Access dashboard
* View audit logs

# Manager
* Manage projects
* Create and assign tasks
* Manage project collaboration
* Manage project documents

# Employee
* View assigned projects/tasks
* Update assigned tasks
* Add comments
* Manage own profile
* Upload relevant documents
---

## Modules

1. **Authentication**

   * Registration, Login, JWT, Refresh Token, Logout, Password Management

2. **User Management**

   * CRUD, Activate/Deactivate Users

3. **RBAC**

   * Admin, Manager and Employee permissions

4. **Project Management**

   * Create, Read, Update, Delete, Search Projects
   * Project Members

5. **Task Management**

   * Create, Read, Update, Delete
   * Assignment, Status, Priority, Due Date, Search

6. **Comments**

   * Add, View, Update and Delete Comments

7. **Document Management**

   * Upload, Download, View, Delete and Search
   * Supported: PDF, DOCX, TXT, CSV

8. **Search**

   * Search Users, Projects, Tasks and Documents
   * Filtering, Sorting and Pagination

9. **Dashboard**

   * Users, Projects, Tasks, Completed/Pending Tasks and Documents statistics

10. **Audit Logs**

    * Track important user, project, task and document activities
---

## Database Entities

User
Role
RefreshToken
Project
ProjectMember
Task
Comment
Document
AuditLog


### Main Relationships

Role → User
User → Projects
Project → Tasks
User → Tasks
Task → Comments
Project → Documents
User → Comments / Documents / AuditLogs

---

## Project Architecture

WorkHUB/
├── app/
│   ├── core/
│   ├── database/
│   ├── models/
│   ├── schemas/
│   ├── routers/
│   ├── services/
│   └── main.py
│
├── alembic/
├── tests/
├── .env
├── .gitignore
├── requirements.txt
└── README.md
---

## Development Flow
Project Setup
     ↓
Configuration
     ↓
PostgreSQL + SQLAlchemy
     ↓
Alembic
     ↓
Authentication
     ↓
User Management
     ↓
RBAC
     ↓
Projects
     ↓
Tasks
     ↓
Comments
     ↓
Documents
     ↓
Search
     ↓
Dashboard
     ↓
Audit Logs
     ↓
Pytest
     ↓
Docker