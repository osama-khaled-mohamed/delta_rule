
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("Perceptron Delta Rule 🎯")

st.subheader("Dataset Input")

data = pd.DataFrame({
    "x1": [0, 0, 1, 1],
    "x2": [0, 1, 0, 1],
    "d1": [0, 1, 1, 1],
    "d2": [0, 0, 0, 1]
})

edited_data = st.data_editor(data)

input_x1 = edited_data["x1"].tolist()
input_x2 = edited_data["x2"].tolist()
d1_target = edited_data["d1"].tolist()
d2_target = edited_data["d2"].tolist()

st.subheader("Initial Weights Input")

col1, col2 = st.columns(2)

with col1:
    st.write("Perceptron 1")
    w1_d1 = st.number_input("weight x1", value=0.1)
    w2_d1 = st.number_input("weight x2", value=0.2)
    b1 = st.number_input("bias 1", value=-0.2)
    threshold_d1 = st.number_input("Threshold 1", value=0.1)

with col2:
    st.write("Perceptron 2")
    w1_d2 = st.number_input("weight x1", value=0.2)
    w2_d2 = st.number_input("weight x2", value=0.3)
    b2 = st.number_input("bias 2", value=1.0)
    threshold_d2 = st.number_input("Threshold 2", value=1.0)

learning_rate = st.number_input("Learning Rate", value=0.1)

def activation(net, threshold):
    return 1 if net >= threshold else 0


def delta_update(w, error, x):
    return w + learning_rate * error * x


def perceptron(x1, x2, w1, w2, b):
    return w1 * x1 + w2 * x2 + b


if st.button("Start Training 🚀"):

    epoch = 0
    stop = False
    errors_per_epoch = []

    while not stop:

        epoch_data = []
        total_errors = 0
        updated = False

        for i in range(len(input_x1)):

            net1 = perceptron(input_x1[i], input_x2[i], w1_d1, w2_d1, b1)
            net2 = perceptron(input_x1[i], input_x2[i], w1_d2, w2_d2, b2)

            y1 = activation(net1, threshold_d1)
            y2 = activation(net2, threshold_d2)

            epoch_data.append([
                input_x1[i], input_x2[i],
                w1_d1, w2_d1, b1,
                net1, d1_target[i], y1,
                w1_d2, w2_d2, b2,
                net2, d2_target[i], y2
            ])

            if y1 != d1_target[i]:
                error = d1_target[i] - y1
                w1_d1 = delta_update(w1_d1, error, input_x1[i])
                w2_d1 = delta_update(w2_d1, error, input_x2[i])
                b1 = delta_update(b1, error, 1)
                updated = True
                total_errors += 1

            if y2 != d2_target[i]:
                error = d2_target[i] - y2
                w1_d2 = delta_update(w1_d2, error, input_x1[i])
                w2_d2 = delta_update(w2_d2, error, input_x2[i])
                b2 = delta_update(b2, error, 1)
                updated = True
                total_errors += 1

        errors_per_epoch.append(total_errors)

        st.subheader(f"Epoch {epoch}")
        columns = [
            "x1", "x2",
            "w13", "w23", "b1",
            "net1", "d1", "y1",
            "w14", "w24", "b2",
            "net2", "d2", "y2"
        ]

        df = pd.DataFrame(epoch_data, columns=columns)
        st.dataframe(df)

        epoch += 1

        if not updated:
            stop = True

    st.subheader("Learning Curve (Errors per Epoch)")

    fig, ax = plt.subplots()
    ax.plot(range(len(errors_per_epoch)), errors_per_epoch, marker='o')
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Number of Errors")
    ax.set_title("Learning Curve")

    st.pyplot(fig)

    st.subheader("Decision Boundary 📊")


    fig, ax = plt.subplots()

   
    for i in range(len(input_x1)):
        if d1_target[i] == 1:
            ax.scatter(input_x1[i], input_x2[i], marker='o', label="Class 1" if i == 0 else "")
        else:
            ax.scatter(input_x1[i], input_x2[i], marker='x', label="Class 0" if i == 0 else "")

    x_vals = np.linspace(-0.5, 1.5, 100)

    if w2_d1 != 0:
        y_vals_d1 = (threshold_d1 - b1 - w1_d1 * x_vals) / w2_d1
        ax.plot(x_vals, y_vals_d1, linestyle='--', label="Boundary d1")

    if w2_d2 != 0:
        y_vals_d2 = (threshold_d2 - b2 - w1_d2 * x_vals) / w2_d2
        ax.plot(x_vals, y_vals_d2, linestyle='-', label="Boundary d2")

    ax.set_xlabel("x1")
    ax.set_ylabel("x2")
    ax.set_title("Decision Boundary")

    ax.legend()

    st.pyplot(fig)
    
st.markdown("---")
st.markdown(
    """
    <div style="
        display: flex;
        justify-content: center;
        margin-top: 30px;
    ">
        <div style="
            padding: 15px 100px;
            border-radius: 0px;
            color: white;
            text-align: center;
            font-size: 16px;
        ">
             <b>DR. Ahmed Maged ------------ Eng. Sohila </b><br>
             <b>Osama Khaled Mohamed --- ID: 22156</b><br>
             
    </div>
    """,
    unsafe_allow_html=True
)
