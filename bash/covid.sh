#!/bin/bash
# This script downloads covid data and displays it
DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
TODAY=$(date)
CURRENT_ICU=$(echo $DATA | jq '.[0].inIcuCurrently')
CURRENT_VENT=$(echo $DATA | jq '.[0].onVentilatorCurrently')
CURRENT_HOSPIT=$(echo $DATA | jq '.[0].hospitalizedCurrently')

echo "On $TODAY, there were $POSITIVE positive COVID cases, $CURRENT_HOSPIT hospitalized currently, $CURRENT_ICU are in the ICU currently and $CURRENT_VENT are currently on a ventilator."

