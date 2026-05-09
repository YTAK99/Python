import tkinter as tk
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.root.geometry("400x250")
        self.root.configure(bg="#1e1e1e")
        self.root.resizable(False, False)

        self.running = False
        self.start_time = 0
        self.elapsed = 0

        # 시간 표시
        self.time_label = tk.Label(
            root,
            text="00:00:00",
            font=("Consolas", 40, "bold"),
            fg="white",
            bg="#1e1e1e"
        )
        self.time_label.pack(pady=40)

        # 버튼 프레임
        button_frame = tk.Frame(root, bg="#1e1e1e")
        button_frame.pack()

        # 시작 버튼
        self.start_btn = tk.Button(
            button_frame,
            text="Start",
            command=self.start,
            width=10,
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            relief="flat",
            cursor="hand2"
        )
        self.start_btn.grid(row=0, column=0, padx=10)

        # 정지 버튼
        self.stop_btn = tk.Button(
            button_frame,
            text="Stop",
            command=self.stop,
            width=10,
            font=("Arial", 12, "bold"),
            bg="#f44336",
            fg="white",
            relief="flat",
            cursor="hand2"
        )
        self.stop_btn.grid(row=0, column=1, padx=10)

        # 리셋 버튼
        self.reset_btn = tk.Button(
            button_frame,
            text="Reset",
            command=self.reset,
            width=10,
            font=("Arial", 12, "bold"),
            bg="#2196F3",
            fg="white",
            relief="flat",
            cursor="hand2"
        )
        self.reset_btn.grid(row=0, column=2, padx=10)

        self.update_timer()

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed

    def stop(self):
        if self.running:
            self.running = False
            self.elapsed = time.time() - self.start_time

    def reset(self):
        self.running = False
        self.elapsed = 0
        self.time_label.config(text="00:00:00")

    def update_timer(self):
        if self.running:
            self.elapsed = time.time() - self.start_time

            hours = int(self.elapsed // 3600)
            minutes = int((self.elapsed % 3600) // 60)
            seconds = int(self.elapsed % 60)

            time_text = f"{hours:02}:{minutes:02}:{seconds:02}"
            self.time_label.config(text=time_text)

        self.root.after(50, self.update_timer)

# 실행
root = tk.Tk()
app = Stopwatch(root)
root.mainloop()
