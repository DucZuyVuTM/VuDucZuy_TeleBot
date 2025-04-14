# Sử dụng image Python chính thức, phiên bản mới nhất
FROM python:3.13-alpine

# Đặt biến môi trường để không lưu bộ đệm khi in
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Tạo thư mục làm việc trong container
WORKDIR /app

# Sao chép file requirements.txt vào container
COPY requirements.txt /app/

# Cài đặt các thư viện cần thiết
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn của bot vào container
COPY . /app/

# Đặt cổng mặc định cho container (tùy chọn, nếu bạn cần expose port)
# EXPOSE 8080

# Khởi động bot Telegram với Procfile (hoặc file chính như bot.py)
CMD ["python", "bot.py"]
