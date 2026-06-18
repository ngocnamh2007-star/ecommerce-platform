# 🛍️ Ecommerce Platform - Bán Hàng Trực Tuyến

Một nền tảng thương mại điện tử hiện đại để bán quần áo, mặt hàng nhu yếu phẩm và các sản phẩm khác.

## ✨ Tính năng chính

- ✅ Quản lý sản phẩm (CRUD)
- ✅ Danh mục sản phẩm
- ✅ Giỏ hàng & thanh toán
- ✅ Quản lý đơn hàng
- ✅ Tài khoản người dùng & xác thực
- ✅ Tìm kiếm & lọc sản phẩm
- ✅ Đánh giá & bình luận sản phẩm
- ✅ Thống kê & báo cáo
- ✅ Admin Panel
- ✅ Gợi ý sản phẩm

## 🏗️ Kiến trúc dự án

```
ecommerce-platform/
├── backend/               # Django REST API
│   ├── manage.py
│   ├── requirements.txt
│   ├── config/            # Settings
│   ├── apps/
│   │   ├── users/        # Quản lý người dùng
│   │   ├── products/     # Quản lý sản phẩm
│   │   ├── orders/       # Quản lý đơn hàng
│   │   ├── cart/         # Giỏ hàng
│   │   └── payments/     # Thanh toán
│   └── utils/            # Hàm tiện ích
├── frontend/             # Next.js + React
│   ├── package.json
│   ├── pages/
│   ├── components/
│   └── styles/
├── docs/                 # Tài liệu
└── docker-compose.yml
```

## 🚀 Công nghệ sử dụng

### Backend
- **Django 4.x** - Web framework
- **Django REST Framework** - API
- **PostgreSQL** - Database
- **Redis** - Cache & Session
- **Celery** - Task queue
- **JWT** - Authentication

### Frontend
- **Next.js 14** - React framework
- **Tailwind CSS** - Styling
- **Axios** - API client
- **Redux Toolkit** - State management

### DevOps
- **Docker** - Containerization
- **Docker Compose** - Orchestration
- **Nginx** - Web server

## 📋 Yêu cầu hệ thống

- Python 3.10+
- Node.js 18+
- PostgreSQL 14+
- Redis 7+
- Docker & Docker Compose

## 🔧 Cài đặt

### 1. Clone Repository
```bash
git clone https://github.com/ngocnamh2007-star/ecommerce-platform.git
cd ecommerce-platform
```

### 2. Setup Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### 3. Setup Frontend
```bash
cd frontend
npm install
npm run dev
```

## 🌐 URLs

- **API**: http://localhost:8000/api/
- **Admin**: http://localhost:8000/admin/
- **Frontend**: http://localhost:3000/

## 📚 API Endpoints

### Users
- `POST /api/users/register/` - Đăng ký
- `POST /api/users/login/` - Đăng nhập
- `GET /api/users/profile/` - Lấy hồ sơ

### Products
- `GET /api/products/` - Danh sách sản phẩm
- `GET /api/products/{id}/` - Chi tiết sản phẩm
- `POST /api/products/` - Tạo sản phẩm (Admin)
- `PUT /api/products/{id}/` - Cập nhật sản phẩm (Admin)
- `DELETE /api/products/{id}/` - Xóa sản phẩm (Admin)

### Orders
- `GET /api/orders/` - Danh sách đơn hàng
- `POST /api/orders/` - Tạo đơn hàng
- `GET /api/orders/{id}/` - Chi tiết đơn hàng

### Cart
- `GET /api/cart/` - Lấy giỏ hàng
- `POST /api/cart/add/` - Thêm vào giỏ hàng
- `DELETE /api/cart/{item_id}/` - Xóa khỏi giỏ hàng

## 🔐 Bảo mật

- JWT Authentication
- Password hashing (bcrypt)
- CORS enabled
- Rate limiting
- Input validation & sanitization

## 📝 Tài liệu API

Xem chi tiết tại: [API Documentation](./docs/API.md)

## 🤝 Contributes

Đóng góp ý kiến: [CONTRIBUTING.md](./CONTRIBUTING.md)

## 📄 License

MIT License - Xem [LICENSE](./LICENSE)

## 👨‍💻 Tác giả

- **Ngô Công Nam** (ngocnamh2007-star)
- Sinh viên Khoa Công Nghệ Thông Tin

---

**Happy Coding!** 🚀
