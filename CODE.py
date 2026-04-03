# import numpy as np

# threshold_d1 = 0.1
# threshold_d2 = 1
# learning_rate = 0.01

# weight_x1_d1 = 0.1
# weight_x2_d1 = 0.2
# bios_d1 = -0.2
# weight_x1_d2 = 0.2
# weight_x2_d2 = 0.3
# bios_d2 = 1

# input_x1=[0,0,1,1]
# input_x2=[0,1,0,1]
# desired_output_d1=[0,1,1,1]
# desired_output_d2=[0,0,0,1]

# net_output_d1=[]
# net_output_d2=[]
# new_weights_d1=[]
# new_weights_d2=[]

# def activation_function(net_output, threshold):
#     return 1 if net_output >= threshold else 0

# def delta_rule_weight_update(weight, error, input_value):
#     return weight + learning_rate * error * input_value

# def perceived_output(x1, x2, weight_x1, weight_x2, bios):
#     return weight_x1 * x1 + weight_x2 * x2 + bios

# def error_calculation(desired_output, perceived_output):
#     return desired_output - perceived_output

# for i in range(len(input_x1)):
#     # Calculate perceived output for d1 and d2
#     net_output_d1[i] = perceived_output(input_x1[i], input_x2[i], weight_x1_d1, weight_x2_d1, bios_d1)
#     net_output_d2[i] = perceived_output(input_x1[i], input_x2[i], weight_x1_d2, weight_x2_d2, bios_d2)
#     # Update weights and bias for d1 only if the output is incorrect
#     if activation_function(net_output_d1[i], threshold_d1) != desired_output_d1[i] :
#         # Calculate error for d1
#         error_d1 = error_calculation(desired_output_d1[i], activation_function(net_output_d1[i], threshold_d1))
#         # Update weights and bias for d1
#         weight_x1_d1 = delta_rule_weight_update(weight_x1_d1, error_d1, input_x1[i])
#         weight_x2_d1 = delta_rule_weight_update(weight_x2_d1, error_d1, input_x2[i])
#         bios_d1 = delta_rule_weight_update(bios_d1, error_d1, 1)
#         new_weights_d1.append((weight_x1_d1, weight_x2_d1, bios_d1))
#     elif activation_function(net_output_d2[i], threshold_d2) != desired_output_d2[i] :
#         # Calculate error for d2
#         error_d2 = error_calculation(desired_output_d2[i], activation_function(net_output_d2[i], threshold_d2))
#         # Update weights and bias for d2
#         weight_x1_d2 = delta_rule_weight_update(weight_x1_d2, error_d2, input_x1[i])
#         weight_x2_d2 = delta_rule_weight_update(weight_x2_d2, error_d2, input_x2[i])
#         bios_d2 = delta_rule_weight_update(bios_d2, error_d2, 1)
#         new_weights_d2.append((weight_x1_d2, weight_x2_d2, bios_d2))
#     else: print("No update needed for both d1 and d2 at index", i)
#     print("Updated weights and bias for d1 at index", new_weights_d1)
#     print("Updated weights and bias for d2 at index", new_weights_d2)












# import numpy as np

# threshold_d1 = 0.1
# threshold_d2 = 1
# learning_rate = 0.01

# weight_x1_d1 = 0.1
# weight_x2_d1 = 0.2
# bias_d1 = -0.2

# weight_x1_d2 = 0.2
# weight_x2_d2 = 0.3
# bias_d2 = 1

# input_x1 = [0, 0, 1, 1]
# input_x2 = [0, 1, 0, 1]

# desired_output_d1 = [0, 1, 1, 1]
# desired_output_d2 = [0, 0, 0, 1]

# new_weights_d1 = []
# new_weights_d2 = []
# counter = 0
# end = False

# def activation_function(net_output, threshold):
#     return 1 if net_output >= threshold else 0


# def delta_rule_weight_update(weight, error, input_value):
#     return weight + learning_rate * error * input_value


# def perceived_output(x1, x2, w1, w2, bias):
#     return w1 * x1 + w2 * x2 + bias


# def error_calculation(target, predicted):
#     return target - predicted
# #for loop and stop when no update needed 
# while end == False: 
     
#     for i in range(len(input_x1)):

#         if i==0: 
#             print("epoch",counter)
#             print("-" * 40)
#         # حساب الناتج
#         net_d1 = perceived_output(input_x1[i], input_x2[i], weight_x1_d1, weight_x2_d1, bias_d1)
#         net_d2 = perceived_output(input_x1[i], input_x2[i], weight_x1_d2, weight_x2_d2, bias_d2)

#         out_d1 = activation_function(net_d1, threshold_d1)
#         out_d2 = activation_function(net_d2, threshold_d2)

#         if out_d1 != desired_output_d1[i]:
#             error_d1 = error_calculation(desired_output_d1[i], out_d1)

#             weight_x1_d1 = delta_rule_weight_update(weight_x1_d1, error_d1, input_x1[i])
#             weight_x2_d1 = delta_rule_weight_update(weight_x2_d1, error_d1, input_x2[i])
#             bias_d1 = delta_rule_weight_update(bias_d1, error_d1, 1)

#             new_weights_d1.append((weight_x1_d1, weight_x2_d1, bias_d1))

#         if out_d2 != desired_output_d2[i]:
#             error_d2 = error_calculation(desired_output_d2[i], out_d2)

#             weight_x1_d2 = delta_rule_weight_update(weight_x1_d2, error_d2, input_x1[i])
#             weight_x2_d2 = delta_rule_weight_update(weight_x2_d2, error_d2, input_x2[i])
#             bias_d2 = delta_rule_weight_update(bias_d2, error_d2, 1)

#             new_weights_d2.append((weight_x1_d2, weight_x2_d2, bias_d2))

#         if out_d1 == desired_output_d1[i] and out_d2 == desired_output_d2[i]:
#             print(f"No update needed at index {i}")
    
#         print(f"d1 weights after index {i}: {weight_x1_d1, weight_x2_d1, bias_d1}")
#         print(f"d2 weights after index {i}: {weight_x1_d2, weight_x2_d2, bias_d2}")
#         print("-" * 40)
#     counter += 1
#     if len(new_weights_d1) == 0 and len(new_weights_d2) == 0:
#         end = True
#     else:
#         new_weights_d1.clear()
#         new_weights_d2.clear()











# import pandas as pd
# import numpy as np
# import pandas as pd

# threshold_d1 = 0.1
# threshold_d2 = 1
# learning_rate = 0.01

# weight_x1_d1 = 0.1
# weight_x2_d1 = 0.2
# bias_d1 = -0.2

# weight_x1_d2 = 0.2
# weight_x2_d2 = 0.3
# bias_d2 = 1

# input_x1 = [0, 0, 1, 1]
# input_x2 = [0, 1, 0, 1]

# desired_output_d1 = [0, 1, 1, 1]
# desired_output_d2 = [0, 0, 0, 1]

# counter = 0
# end = False


# def activation_function(net_output, threshold):
#     return 1 if net_output >= threshold else 0


# def delta_rule_weight_update(weight, error, input_value):
#     return weight + learning_rate * error * input_value


# def perceived_output(x1, x2, w1, w2, bias):
#     return w1 * x1 + w2 * x2 + bias


# def error_calculation(target, predicted):
#     return target - predicted


# while end == False:

#     epoch_data = []  # لتخزين الجدول

#     print(f"\nEpoch {counter}")
#     print("=" * 60)

#     updated = False  # نتابع هل حصل update ولا لا

#     for i in range(len(input_x1)):

#         net_d1 = perceived_output(input_x1[i], input_x2[i], weight_x1_d1, weight_x2_d1, bias_d1)
#         net_d2 = perceived_output(input_x1[i], input_x2[i], weight_x1_d2, weight_x2_d2, bias_d2)

#         out_d1 = activation_function(net_d1, threshold_d1)
#         out_d2 = activation_function(net_d2, threshold_d2)

#         # حفظ القيم قبل التحديث
#         row = [
#             input_x1[i], input_x2[i],
#             weight_x1_d1, weight_x2_d1, bias_d1,
#             net_d1, desired_output_d1[i], out_d1,
#             weight_x1_d2, weight_x2_d2, bias_d2,
#             net_d2, desired_output_d2[i], out_d2
#         ]

#         epoch_data.append(row)

#         # تحديث d1
#         if out_d1 != desired_output_d1[i]:
#             error_d1 = error_calculation(desired_output_d1[i], out_d1)

#             weight_x1_d1 = delta_rule_weight_update(weight_x1_d1, error_d1, input_x1[i])
#             weight_x2_d1 = delta_rule_weight_update(weight_x2_d1, error_d1, input_x2[i])
#             bias_d1 = delta_rule_weight_update(bias_d1, error_d1, 1)

#             updated = True

#         # تحديث d2
#         if out_d2 != desired_output_d2[i]:
#             error_d2 = error_calculation(desired_output_d2[i], out_d2)

#             weight_x1_d2 = delta_rule_weight_update(weight_x1_d2, error_d2, input_x1[i])
#             weight_x2_d2 = delta_rule_weight_update(weight_x2_d2, error_d2, input_x2[i])
#             bias_d2 = delta_rule_weight_update(bias_d2, error_d2, 1)

#             updated = True

#     # إنشاء الجدول
#     columns = [
#         "x1", "x2",
#         "w1_d1", "w2_d1", "b1",
#         "net1", "d1", "y1",
#         "w1_d2", "w2_d2", "b2",
#         "net2", "d2", "y2"
#     ]

#     df = pd.DataFrame(epoch_data, columns=columns)
#     print(df)

#     counter += 1

#     # شرط الإيقاف
#     if not updated:
#         end = True




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