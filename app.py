import streamlit as st
import random

# 問題と答えのリスト
questions = [
    {"question": "問題1", "choices": ["選択肢1", "選択肢2", "選択肢3", "選択肢4"], "answer": "選択肢1"},
    # 他の問題を追加
]

random.shuffle(questions)  # 問題をランダムにする
questions = questions[:10]  # 最初の10問だけを取る

answers = []
for i, q in enumerate(questions):
    st.write(f"問題 {i+1}: {q['question']}")
    answer = st.radio(f"回答 {i+1}:", q['choices'])
    answers.append(answer)

if st.button("回答を送信する"):
    correct_answers = sum(a == b for a, b in zip(answers, [q['answer'] for q in questions]))
    st.write(f"終了！あなたの正答数は {correct_answers} / 10 です。")
    st.write(f"正答率は {correct_answers * 10}% です。")
