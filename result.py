import streamlit as st
import joblib


def app():
    model = joblib.load('log.model')

    if 'submited_form' not in st.session_state:
        test_x = None
    else:
        test_x = st.session_state.submited_form

    if test_x is not None:
        rs_prob = model.predict_proba(test_x)
        rs = model.predict(test_x)

        prob = rs_prob[0][1]

        st.markdown('Probability of Approval: {:.2%}'.format(prob))

        if rs[0] == 1:
            st.markdown('Congratulations! Your application is very likely to succeed!')
        else:
            st.markdown('It looks like your application is going to fail.')
            """
                0 debt_to_income_ratio_60,
                1 income,
                2 load_amount,
                3 property_value,
                4 open_end_line_of_credit,
                5 debt_to_income_ratio_50,
                6 co_applicant_credit_score_type_9,
                7 co_applicant_age_above_62,
                8 lien_status,
            """

            text_x = test_x[0]

            st.markdown('Below are the suggestions provided based on your info:')

            if text_x[0] == 1:
                st.markdown('- Decrease the debt to income ratio')

            if text_x[4] == 0:
                st.markdown('- Select the loan that covered by open-end line of credit')

            st.markdown('- Acquire higher property value')
            st.markdown('- Decrease your loan amount')

    else:
        st.markdown('Please submit your information first.')
