import streamlit as st
import random

# 問題と答えのリスト
questions_j = [
    {"question": "問1：A～Cに当てはまる言葉を下記の語群から選び、文章を完成させましょう。人が痩せる仕組みで考えられ理由は大きく二つと考えられます。一つは（　A　）、もう一つは（　B　）にあるということ。この二つの理由は必ずしも、からだにとって「良い状態」ではない。一般的にダイエットとは、この二つの理由を人為的に作り出して痩せさせていくものでその負担は、からだにとってどのくらいのものなのかを知り、（　C　）なダイエットをしなくてはいけない。", "choices": ["①A:発汗,B:飢餓状態,C:健康的", "②A:臓器の故障,B:飢餓状態,C:活動的", "③A:臓器の故障,B:代謝異常,C:健康的", "④A:臓器の故障,B:飢餓状態,C:健康的"], "answer": "④A:臓器の故障,B:飢餓状態,C:健康的"},
    {"question": "問2：基礎代謝（量）という言葉の正確な定義を下記から選んでください。", "choices": ["①今日一日生きるために最低限必要なエネルギー", "②細胞の生まれ変わりをあらわす", "③汗をかくこと"], "answer": "①今日一日生きるために最低限必要なエネルギー"},
    {"question": "問3：A～Cに当てはまる言葉を下記の語群から選び、文章を完成させましょう。一日の全消費エネルギーの約（　A　）％が基礎代謝で消費され、消費エネルギーが最も多い部分は（　B　）で約（　C　）％消費している。", "choices": ["①A:60,B:血液,C:40", "①A:50,B:筋肉,C:40", "①A:60,B:筋肉,C:40", "①A:60,B:骨,C:50"], "answer": "①A:60,B:筋肉,C:40"}
    # 他の問題を追加
]

#random.shuffle(questions)  # 問題をランダムにする
#questions = questions[:10]  # 最初の10問だけを取る

st.title('ジュニア＆レギュラー復習問題')
st.write('ジュニアダイエットマスター復習問題')

answers = []
for i, q in enumerate(questions):
    st.write(f"問題 {i+1}: {q['question']}")
    answer = st.radio(f"回答 {i+1}:", q['choices'])
    answers.append(answer)

if st.button("回答を送信する"):
    correct_answers = sum(a == b for a, b in zip(answers, [q['answer'] for q in questions]))
    st.markdown(f"## 終了！あなたの正答数は {correct_answers} / 10 です。")
    st.markdown(f"# 正答率は **{correct_answers * 10}%** です！")
