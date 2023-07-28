import tkinter as tk
from tkinter import messagebox
import time
import winsound

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Alarm Clock")

        self.alarms = []
        self.current_alarm = None

        self.time_label = tk.Label(root, text="", font=("Helvetica", 48))
        self.time_label.pack(pady=20)

        self.set_alarm_label = tk.Label(root, text="Set Alarm (HH:MM):")
        self.set_alarm_label.pack()

        self.set_alarm_entry = tk.Entry(root)
        self.set_alarm_entry.pack()

        self.set_alarm_button = tk.Button(root, text="Set Alarm", command=self.set_alarm)
        self.set_alarm_button.pack(pady=10)

        self.cancel_alarm_button = tk.Button(root, text="Cancel Alarm", command=self.cancel_alarm, state=tk.DISABLED)
        self.cancel_alarm_button.pack(pady=5)

        self.update_time()
        self.check_alarms()

    def update_time(self):
        current_time = time.strftime("%H:%M:%S")
        self.time_label.config(text=current_time)
        self.root.after(1000, self.update_time)

    def set_alarm(self):
        alarm_time = self.set_alarm_entry.get()
        try:
            alarm_seconds = sum(int(x) * 60 ** i for i, x in enumerate(reversed(alarm_time.split(":"))))
            self.alarms.append((alarm_time, alarm_seconds))
            messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")
            self.set_alarm_entry.delete(0, tk.END)
            self.cancel_alarm_button.config(state=tk.NORMAL)
        except ValueError:
            messagebox.showerror("Error", "Invalid time format. Use HH:MM")

    def cancel_alarm(self):
        if self.current_alarm:
            self.alarms.remove(self.current_alarm)
            self.current_alarm = None
            self.cancel_alarm_button.config(state=tk.DISABLED)

    def check_alarms(self):
        current_seconds = sum(int(x) * 60 ** i for i, x in enumerate(reversed(time.strftime("%H:%M").split(":"))))

        for alarm in self.alarms:
            if alarm[1] == current_seconds:
                self.current_alarm = alarm
                winsound.Beep(500, 2000)  # Beep for 2 seconds (adjust frequency and duration as needed)
                messagebox.showinfo("Alarm", f"Time's up! Alarm set for {alarm[0]}")
                self.cancel_alarm()

        self.root.after(1000, self.check_alarms)

if __name__ == "__main__":
    root = tk.Tk()
    alarm_clock = AlarmClock(root)
    root.mainloop()
