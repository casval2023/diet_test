import streamlit as st
import random

# 問題と答えのリスト
questions = [
    {"question": "問題1", "choices": ["選択肢1", "選択肢2", "選択肢3", "選択肢4"], "answer": "選択肢1"},
    # 他の問題を追加
]

random.shuffle(questions)  # 問題をランダムにする
questions = questions[:10]  # 最初の10問だけを取る

correct_answers = 0

for i, q in enumerate(questions):
    st.write(f"問題 {i+1}: {q['question']}")
    answer = st.radio("回答:", q['choices'])

    if st.button("回答する"):
        if answer == q['answer']:
            st.write("正解！")
            correct_answers += 1
        else:
            st.write(f"不正解。正解は {q['answer']} です。")

st.write(f"終了！あなたの正答数は {correct_answers} / 10 です。")
st.write(f"正答率は {correct_answers * 10}% です。")
