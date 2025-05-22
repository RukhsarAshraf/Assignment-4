import streamlit as st

st.set_page_config(page_title="📚 Student Grade Visualizer", layout="centered")

st.title("📚 Student Grade Visualizer")
st.write("Enter your subjects and marks to see your result:")

# Select number of subjects
num_subjects = st.slider("How many subjects?", 2, 10, 5)

subject_names = []
marks = []

# Input fields for each subject
for i in range(num_subjects):
    col1, col2 = st.columns([2, 1])
    with col1:
        subject = st.text_input(f"Subject {i+1} Name", key=f"subject_{i}")
    with col2:
        mark = st.number_input(f"Marks for {subject or f'Subject {i+1}'}", 0, 100, key=f"mark_{i}")
    
    subject_names.append(subject or f"Subject {i+1}")
    marks.append(mark)

# Function for grading
def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"

# Show result
if st.button("Calculate Result"):
    total = sum(marks)
    avg = total / num_subjects
    grade = get_grade(avg)

    st.success(f"✅ Total Marks: **{total}**")
    st.info(f"📊 Average Percentage: **{avg:.2f}**")
    st.warning(f"🎓 Grade: **{grade}**")
    st.balloons()