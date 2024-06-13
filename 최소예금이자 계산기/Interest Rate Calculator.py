import tkinter as tk
import tkinter.font as tkFont

def calc_InterestRate():
    try:
        InflationRate = float(input_InflationRate.get())
        TaxRate = 0.154
        min_InterestRate = InflationRate / (1 - TaxRate)
        result_message = ("[ 결 과 ]\n\n"
                          f"- 입력한 물가상승률: {InflationRate:.2f}%\n"
                          f"- 적용된 이자소득세율: {TaxRate * 100:.2f}%\n"
                          f"- 계산된 최소 예금 이자: {min_InterestRate:.2f}%\n\n"
                          f"물가상승률을 고려했을 때, 예금이자는 최소 {min_InterestRate:.2f}% 이상이 되어야 함")
        text_result.config(state=tk.NORMAL)  # 편집 가능 상태로 변경
        text_result.delete("1.0", tk.END)   # 기존 텍스트 삭제
        text_result.insert(tk.END, result_message)  # 새로운 결과 메시지 삽입
        text_result.config(state=tk.DISABLED)  # 편집 불가능 상태로 변경
    except ValueError:
        text_result.config(state=tk.NORMAL)
        text_result.delete("1.0", tk.END)
        text_result.insert(tk.END, "유효한 숫자를 입력하세요.")
        text_result.config(state=tk.DISABLED)

# 메인윈도우
root = tk.Tk()
root.title("최소예금이자 계산기")
root.geometry("400x320")

# 상단 설명
label_Desc = tk.Label(root, text="[ 최소예금이자 ]\n\n소비자 물가상승률과 이자소득세를 반영한 이자를 의미", wraplength=380)
label_Desc.pack(pady=10)

# 현재 물가상승률 입력
label_InterestRate = tk.Label(root, text="물가상승률(%):")
label_InterestRate.pack(pady=5)
input_InflationRate= tk.Entry(root)
input_InflationRate.pack(pady=5)

# 버튼
button_calc = tk.Button(root, text="계산하기", command=calc_InterestRate)
button_calc.pack(pady=10)

# 하단 결과
font=tkFont.Font(family="맑은 고딕", size=9)
text_result = tk.Text(root, wrap=tk.WORD, height=8, font=font, state=tk.DISABLED)
text_result.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

root.mainloop()
