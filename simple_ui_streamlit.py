import streamlit as st
import numpy as np
import pandas as pd
import repository
from dotenv import load_dotenv
import constants
import os
from datetime import datetime


load_dotenv()
constants.SCALYR_TOKEN = os.environ["SCALYR_TOKEN"]

def get_log_by_trace_id(trace_id):
    if trace_id == "":
        st.error("please enter trace id")
        return
    logs = repository.get_log_by_trace_id(trace_id)
    if logs == None:
        st.write("logs not found")
        return
    df = pd.DataFrame(logs)
    df = df[["severity", "message", "timestamp"]]
    st.table(df)

st.set_page_config(layout="wide")
st.title("WELCOME TO SPACELOG")
trace_id = st.text_input("trace id", help="please enter the trace ID for the log you wish to retrieve.")
if st.button("get log"):
    get_log_by_trace_id(trace_id)
