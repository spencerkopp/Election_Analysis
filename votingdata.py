voting_data = []
voting_data.append({'county':'Arapahoe', 'registered_voters': 422829})
voting_data.append({'county':'Denver', 'registered_voters': 463353})
voting_data.append({'county':'Jefferson', 'registered_voters': 432438})
for i in range(len(voting_data)):
    print(f"{voting_data[i]['county']}county has{voting_data[i]['registered_voters']}registered voters.")