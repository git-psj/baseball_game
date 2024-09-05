
import streamlit as st
import random

def generate_number():
    """Generate a random 3-digit number with unique digits"""
    return ''.join(random.sample('123456789', 3))

def get_feedback(guess, number):
    """Give feedback in terms of strikes and balls"""
    strikes = sum(g == n for g, n in zip(guess, number))
    balls = len(set(guess) & set(number)) - strikes
    return strikes, balls

def main():
    st.title("숫자 야구 게임")
    st.write("세 자리 숫자를 맞추는 게임입니다. 숫자는 중복되지 않으며, 각각의 자리에서 맞춘 숫자의 개수를 스트라이크, 맞춘 숫자의 개수를 볼로 알려드립니다.")
    
    if 'number' not in st.session_state:
        st.session_state.number = generate_number()
        st.session_state.attempts = 0

    guess = st.text_input("추측한 숫자를 입력하세요 (예: 123)", max_chars=3)
    
    if st.button("제출"):
        if not guess.isdigit() or len(guess) != 3 or len(set(guess)) != 3:
            st.error("숫자는 3자리이어야 하며, 중복되지 않아야 합니다.")
        else:
            strikes, balls = get_feedback(guess, st.session_state.number)
            st.session_state.attempts += 1

            if strikes == 3:
                st.success(f"축하합니다! 정답을 맞추셨습니다! 정답은 {st.session_state.number}였으며, 총 시도 횟수는 {st.session_state.attempts}회입니다.")
                st.session_state.number = generate_number()  # 새로운 게임 시작
                st.session_state.attempts = 0
            else:
                st.write(f"{strikes} 스트라이크, {balls} 볼")

    if st.button("게임 리셋"):
        st.session_state.number = generate_number()
        st.session_state.attempts = 0
        st.write("게임이 리셋되었습니다. 새로운 숫자를 맞춰보세요!")

if __name__ == "__main__":
    main()
