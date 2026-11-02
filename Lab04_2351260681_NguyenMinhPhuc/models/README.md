# Offline Vietnamese neural TTS voice

The notebook's optional neural backend uses Piper's Vietnamese `vais1000` medium ONNX voice. The model is approximately 63 MB and is intentionally not committed to Git. Its voice files are distributed from the official Piper voices repository under the voice's MIT license; the Piper inference runtime is a separate dependency.

Download the model and matching config into this folder:

```powershell
New-Item -ItemType Directory -Force models | Out-Null
Invoke-WebRequest https://huggingface.co/rhasspy/piper-voices/resolve/main/vi/vi_VN/vais1000/medium/vi_VN-vais1000-medium.onnx -OutFile models/vi_VN-vais1000-medium.onnx
Invoke-WebRequest https://huggingface.co/rhasspy/piper-voices/resolve/main/vi/vi_VN/vais1000/medium/vi_VN-vais1000-medium.onnx.json -OutFile models/vi_VN-vais1000-medium.onnx.json
```

Then install `piper-tts` from `requirements.txt`. The wrapper reads this relative project path or the `PIPER_MODEL` environment variable. No model download is performed by the notebook.
