# Nhận dạng lệnh tiếng Việt cô lập — Lab 3

Dự án triển khai hệ thống nhận dạng năm lệnh tiếng Việt từ tệp âm thanh WAV bằng MFCC và mô hình Hidden Markov Gaussian (HMM) trái sang phải. Notebook cũng đánh giá mô hình bằng ma trận nhầm lẫn, biểu đồ đường đi Viterbi và so sánh với phương pháp DTW.

## Bắt đầu nhanh

1. Cài Python 3.10 trở lên.
2. Mở terminal tại thư mục gốc của dự án.
3. Cài các thư viện cần thiết:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Mở `Lab03.ipynb` trong Jupyter và chạy lần lượt tất cả các cell. Nếu cell cài đặt thư viện yêu cầu khởi động lại kernel, hãy khởi động lại rồi chạy notebook từ đầu.

## Dữ liệu

Mặc định, notebook tìm thư mục `dataset/` nằm cạnh notebook. Vì vậy, khi sao chép hoặc clone dự án, hãy đặt dữ liệu theo cấu trúc sau:

```text
dataset/
  metadata.csv
  README.txt
  train/     # Các tệp WAV dùng để huấn luyện
  test/      # Các tệp WAV dùng để kiểm tra
```

Không cần cấu hình đường dẫn riêng theo máy. Nếu muốn lưu dữ liệu ở nơi khác, đặt biến môi trường `LAB3_DATA_DIR` trỏ đến thư mục chứa `metadata.csv`, `train/` và `test/`.

`lexicon.txt` liệt kê năm nhãn lệnh và cách viết tiếng Việt. Dữ liệu được cung cấp là giọng tổng hợp eSpeak TTS, không phải ghi âm người thật. Tập kiểm tra nhỏ chỉ dùng để minh họa pipeline, không đại diện cho độ chính xác trong môi trường thực tế.

## Kết quả

Notebook lưu mô hình đã huấn luyện tại `models/hmm_models.joblib` và các kết quả đánh giá trong `outputs/`, gồm ma trận nhầm lẫn, biểu đồ trạng thái Viterbi, điểm likelihood theo từng tệp và bảng so sánh DTW với HMM. Báo cáo tiếng Việt được cung cấp trong `Lab3_Report.pdf`.

## Khả năng tái lập

Notebook sử dụng phân chia train/test trong `metadata.csv`. Thống kê CMVN chỉ được ước lượng từ các frame huấn luyện. Số trạng thái HMM và kiểu covariance có thể điều chỉnh trong cell huấn luyện.

Thử nghiệm bigram cần có corpus gồm các chuỗi lệnh thực tế. Bộ dữ liệu hiện tại chỉ chứa các lệnh riêng lẻ, nên notebook không tự tạo thống kê bigram từ nhãn tập test.
