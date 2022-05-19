import streamlit as st
import joblib
import global_var


def app():

    model = joblib.load('log.model.pkl')

    with st.form("my_form"):

        st.subheader("Start your prediction")

        income = st.number_input('Please input your estimated Gross Annual Income (in thousands)')
        load_amount = st.number_input('Please input your estimated Loan Amount')
        property_value = st.number_input('Please input your estimated Total Property Value')
        open_end_line_of_credit = st.radio(
            'The covered loan application is for an open-end line of credit', [True, False])
        co_applicant_credit_score_type = st.radio(
            'The credit score type of your co-applicant is applicable',
            [True, False])
        co_applicant_age_above62 = st.radio('Your co-applicant age is above 62',
                                            [True, False])

        lien_status = st.radio(
            'Please select your lien status',
            ['0 - secured by a subordinate lien','1 - secured by a first lien'])
        debt_to_income_ratio = st.radio('Please select your Debt to Income Ratio (Total Monthly Debt ➗ Total Monthly Income)',
                                        ['>60%', '36% - 50%','Others'])

        if open_end_line_of_credit:
            open_end_line = 1
        else:
            open_end_line = 0

        if debt_to_income_ratio == '>60%':
            debt_to_income_ratio_60 = 1
            debt_to_income_ratio_50 = 0
        elif debt_to_income_ratio == '36%-<50%':
            debt_to_income_ratio_60 = 0
            debt_to_income_ratio_50 = 1
        else:
            debt_to_income_ratio_60 = 0
            debt_to_income_ratio_50 = 0

        if lien_status == '0 - secured by a subordinate lien':
            lien_status = 0
        else:
            lien_status = 1 


        co_applicant_credit_score_type_9 = 0 if co_applicant_credit_score_type else 1  # noqa

        co_applicant_age_above_62 = 1 if co_applicant_age_above62 else 0

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:

            submited_form = [[
                debt_to_income_ratio_60,
                income,
                load_amount,
                property_value,
                open_end_line,
                debt_to_income_ratio_50,
                co_applicant_credit_score_type_9,
                co_applicant_age_above_62,
                lien_status,
            ]]

            global_var.set_value('submited_form', submited_form)

            st.session_state.submited_form = submited_form

            st.success(
                'Application submited. Please check your application at result page!'  # noqa
            )
