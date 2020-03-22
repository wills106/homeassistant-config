STARTDATE=`date -d @$(( $(date +"%s") - 86400)) +"%Y-%m-%dT00:00:00"`
ENDDATE=`date -d @$(( $(date +"%s") - 86400)) +"%Y-%m-%dT23:59:59"`
STARTDATEPREV=`date -d @$(( $(date +"%s") - 172800)) +"%Y-%m-%dT00:00:00"`
ENDDATEPREV=`date -d @$(( $(date +"%s") - 172800)) +"%Y-%m-%dT23:59:59"`
COUNT=`curl -H "Authorization: Basic API_KEY" "https://api.octopus.energy/v1/gas-meter-points/MPAN/meters/SERIAL/consumption/?period_from=$STARTDATE&period_to=$ENDDATE" | python -mjson.tool | grep -c "consumption"`

if [[ "$COUNT" == 48 ]]
then
curl -H "Authorization: Basic API_KEY" "https://api.octopus.energy/v1/gas-meter-points/MPAN/meters/SERIAL/consumption/?period_from=$STARTDATE&period_to=$ENDDATE" | jq '[.. | objects | .consumption] | add' | awk '{printf "%0.2f\n",$1}' 
else
curl -H "Authorization: Basic API_KEY" "https://api.octopus.energy/v1/gas-meter-points/MPAN/meters/SERIAL/consumption/?period_from=$STARTDATEPREV&period_to=$ENDDATEPREV" | jq '[.. | objects | .consumption] | add' | awk '{printf "%0.2f\n",$1}'  
fi