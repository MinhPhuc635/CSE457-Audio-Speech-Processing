# Lab 5 — CSE457

**Sinh viên:** Nguyễn Minh Phúc (2351260681)

## Cấu trúc

- `Lab5.ipynb`: notebook theo Task 0–8; chạy toàn bộ cell tuần tự.
- `lab5_dataset/`: clean, noise và separation WAV. Dataset hiện không có manifest hoặc mixing-matrix metadata.
- `results/audio/`: noisy, enhanced, mixture và separated WAV; separated được peak-normalize, hai mixture microphone dùng chung gain.
- `results/figures/`: spectrogram, confusion matrix, FAR–FRR, tương quan ICA.
- `results/*.csv`: số liệu enhancement, speaker-ID và ablation.
- `Bao_cao_Lab05.docx`: report cập nhật theo dataset hiện tại, gồm câu trả lời 12 câu hỏi ở cuối.

## Môi trường

Python 3.10+; dependencies:

```bash
python -m pip install numpy scipy matplotlib soundfile scikit-learn pandas jupyter nbclient python-docx
```

## Chạy

Mở thư mục `Lab05_2351260681_NguyenMinhPhuc` làm working directory rồi chạy `Lab5.ipynb` từ trên xuống. Notebook cũng nhận diện working directory là thư mục gốc repository. Tham số thí nghiệm nằm ở Task 0; seed ICA cố định để tái lập.

## Phạm vi dữ liệu speaker

Dataset hiện có enrollment/test cho spk01, spk02 và spk03. Mỗi người có bốn enrollment, trong đó ba mẫu dùng train speaker verification và enrollment_04 được giữ làm dev; test gồm hai mẫu mỗi người. Vì không có manifest, notebook khám phá split từ tên file. Ma trận mixing dùng các giá trị ví dụ trong đề Lab 5.
