import streamlit as st

st.set_page_config(
    page_title="Calculator",
    page_icon="🧮",
    layout="centered"
)

# -----------------------------
# تنسيق الحاسبة
# -----------------------------
st.markdown("""
<style>

.main {
    padding-top: 30px;
}

.calculator {
    max-width: 500px;
    margin: auto;
}

div.stButton > button {
    width: 100%;
    height: 70px;
    border-radius: 18px;
    font-size: 25px;
    font-weight: bold;
    border: none;
}

input {
    text-align: right !important;
    font-size: 30px !important;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# المتغيرات
# -----------------------------
if "display" not in st.session_state:
    st.session_state.display = "0"

if "first_number" not in st.session_state:
    st.session_state.first_number = None

if "operator" not in st.session_state:
    st.session_state.operator = None


# -----------------------------
# دالة الضغط على الأزرار
# -----------------------------
def press(button):

    # مسح
    if button == "C":
        st.session_state.display = "0"
        st.session_state.first_number = None
        st.session_state.operator = None

    # حذف آخر رقم
    elif button == "⌫":
        if len(st.session_state.display) > 1:
            st.session_state.display = st.session_state.display[:-1]
        else:
            st.session_state.display = "0"

    # الأرقام
    elif button in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:

        if st.session_state.display == "0":
            st.session_state.display = button
        else:
            st.session_state.display += button

    # الفاصلة
    elif button == ".":

        if "." not in st.session_state.display:
            st.session_state.display += "."

    # العمليات
    elif button in ["+", "-", "×", "÷"]:

        st.session_state.first_number = float(
            st.session_state.display
        )

        st.session_state.operator = button

        st.session_state.display = "0"

    # النتيجة
    elif button == "=":

        if (
            st.session_state.first_number is not None
            and st.session_state.operator is not None
        ):

            second_number = float(st.session_state.display)

            operation = st.session_state.operator

            if operation == "+":
                result = st.session_state.first_number + second_number

            elif operation == "-":
                result = st.session_state.first_number - second_number

            elif operation == "×":
                result = st.session_state.first_number * second_number

            elif operation == "÷":

                if second_number == 0:
                    st.session_state.display = "Error"
                    return

                result = st.session_state.first_number / second_number

            # إزالة .0 إذا الرقم صحيح
            if result == int(result):
                result = int(result)

            st.session_state.display = str(result)

            st.session_state.first_number = None
            st.session_state.operator = None

    # النسبة
    elif button == "%":

        number = float(st.session_state.display)

        result = number / 100

        if result == int(result):
            result = int(result)

        st.session_state.display = str(result)


# -----------------------------
# عنوان
# -----------------------------
st.markdown(
    "<h1 style='text-align:center;'>🧮 الحاسبة</h1>",
    unsafe_allow_html=True
)


# -----------------------------
# شاشة الحاسبة
# -----------------------------
st.text_input(
    "display",
    value=st.session_state.display,
    disabled=True,
    label_visibility="collapsed"
)

st.write("")


# -----------------------------
# أزرار الحاسبة
# -----------------------------
rows = [
    ["C", "⌫", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["00", "0", ".", "="]
]


for row in rows:

    columns = st.columns(4)

    for i, button in enumerate(row):

        with columns[i]:

            if st.button(
                button,
                key=f"button_{button}_{rows.index(row)}"
            ):

                if button == "00":

                    if st.session_state.display == "0":
                        st.session_state.display = "0"
                    else:
                        st.session_state.display += "00"

                else:
                    press(button)

                st.rerun()
