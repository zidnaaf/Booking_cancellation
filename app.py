import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open('ran_forest_model.sav', 'rb')) # Reading the binary format


# Creating a function for prediction

def cancellation_prediction(input_data):
    
    # change the input data to numpy array
    input_data_np = np.asarray(input_data)

    # Reshape the array
    input_data_reshape = input_data_np.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshape)
    print(prediction)

    if (prediction[0] == 0):
        return 'The Booking order is cancelled'
    else:
        return 'The Booking order is not cancelled'


def main():

    # Give title
    st.title('Booking Cancellation Prediction')

    # Get the input data

    required_car_parking_space = st.selectbox('Using the parking space', ('Yes', 'No'))
    lead_time = st.text_input('The Booking Lead Time')
    repeated_guest = st.selectbox('Is the customer a repeated guest?', ('Yes', 'No'))
    no_of_previous_cancellations = st.text_input('Number of previous bookings that were canceled')
    no_of_previous_bookings_not_canceled = st.text_input('Number of previous bookings that were not canceled')
    avg_price_per_room = st.text_input('Average price per day of the reservation (in euro)')
    no_of_special_requests = st.text_input('Total number of special requests')
    total_guests = st.text_input('Number of guests')
    total_night = st.text_input('Total stay')
    Holidays = st.selectbox('Is the customer stay on Holidays', ('Yes', 'No'))
    Type_of_meal = st.selectbox("Type of meal booked by customer", ('Plan 1', 'Plan 2', 'Plan 3', 'Nothing'))
    Room_type = st.selectbox("Type of room booked by customer", ('Type 1', 'Type 2', 'Type 3', 'Type 4', 'Type 5', 'Type 6', 'Type 7'))
    Segment = st.selectbox ('Market segment', ('Aviation', 'Complementary', 'Corporate', 'Offline', 'Online'))

    # Parking space
    if required_car_parking_space == 'Yes':
        required_car_parking_space = 1
    else:
        required_car_parking_space = 0

    # Repeated guests
    if repeated_guest == 'Yes':
        repeated_guest = 1
    else:
        repeated_guest = 0

    # Holidays
    if Holidays == 'Yes':
        Holidays = 0
    else:
        Holidays = 1
    
    
    # Booked meal type
    if Type_of_meal == 'Plan 1':
        ToM_plan_1 = 1
    else:
        ToM_Plan_2 = 0
        ToM_Plan_3 = 0
        ToM_Plan_NS = 0

    if Type_of_meal == 'Plan 2':
        ToM_plan_2 = 1
    else:
        ToM_Plan_1 =0
        ToM_Plan_3 = 0
        ToM_Plan_NS = 0

    if Type_of_meal == 'Plan 3':
        ToM_plan_3 = 1
    else:
        ToM_Plan_2 = 0
        ToM_Plan_1 = 0
        ToM_Plan_NS = 0

    if Type_of_meal == 'Nothing':
        ToM_plan_NS = 1
    else:
        ToM_Plan_2 = 0
        ToM_Plan_3 = 0
        ToM_Plan_1 = 0
    # Room Type
    if Room_type == 'Type 1':
        Room_type_1 = 1
    else:
        Room_type_2 = 0
        Room_type_3 = 0
        Room_type_4 = 0
        Room_type_5 = 0
        Room_type_6 = 0
        Room_type_7 = 0

    if Room_type == 'Type 2':
        Room_type_2 = 1
    else:
        Room_type_1 = 0
        Room_type_3 = 0
        Room_type_4 = 0
        Room_type_5 = 0
        Room_type_6 = 0
        Room_type_7 = 0
    
    if Room_type == 'Type 3':
        Room_type_3 = 1
    else:
        Room_type_2 = 0
        Room_type_1 = 0
        Room_type_4 = 0
        Room_type_5 = 0
        Room_type_6 = 0
        Room_type_7 = 0
    
    if Room_type == 'Type 4':
        Room_type_4 = 1
    else:
        Room_type_2 = 0
        Room_type_3 = 0
        Room_type_1 = 0
        Room_type_5 = 0
        Room_type_6 = 0
        Room_type_7 = 0
    
    if Room_type == 'Type 5':
        Room_type_5 = 1
    else:
        Room_type_2 = 0
        Room_type_3 = 0
        Room_type_4 = 0
        Room_type_1 = 0
        Room_type_6 = 0
        Room_type_7 = 0
    
    if Room_type == 'Type 6':
        Room_type_6 = 1
    else:
        Room_type_2 = 0
        Room_type_3 = 0
        Room_type_4 = 0
        Room_type_5 = 0
        Room_type_1 = 0
        Room_type_7 = 0
    
    if Room_type == 'Type 7':
        Room_type_7 = 1
    else:
        Room_type_2 = 0
        Room_type_3 = 0
        Room_type_4 = 0
        Room_type_5 = 0
        Room_type_6 = 0
        Room_type_1 = 0

    #Segment
    if Segment == 'Aviation':
        Aviation = 1
    else:
        Complementary = 0
        Corporate = 0
        Offline = 0
        Online = 0

    if Segment == 'Complementary':
        Complementary = 1
    else:
        Aviation = 0
        Corporate = 0
        Offline = 0
        Online = 0

    if Segment == 'Corporate':
        Corporate = 1
    else:
        Aviation = 0
        Complementary = 0
        Offline = 0
        Online = 0

    if Segment == 'Offline':
        Offline = 1
    else:
        Aviation = 0
        Complementary = 0
        Corporate = 0
        Online = 0

    if Segment == 'Online':
        Online = 1
    else:
        Aviation = 0
        Complementary = 0
        Offline = 0
        Corporate = 0

    # Code for prediction
    cancellation = ''

    # Create a button for prediction
    if st.button('Booking Status'):
        cancellation = cancellation_prediction([required_car_parking_space, lead_time, repeated_guest, no_of_previous_cancellations,
                                                no_of_previous_bookings_not_canceled, avg_price_per_room, no_of_special_requests, total_guests,
                                                total_night, Holidays, 
                                                ToM_plan_1, ToM_Plan_2, ToM_Plan_3, ToM_Plan_NS, Room_type_1, Room_type_2,
                                                Room_type_3, Room_type_4, Room_type_5, Room_type_6, Room_type_7, Aviation, Complementary, Corporate,
                                                Offline, Online])

    st.success(cancellation)


if __name__ == '__main__':
    main()