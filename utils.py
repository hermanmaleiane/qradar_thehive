from datetime import datetime,timedelta


def format_description (description,rules,severity, source_network, destination_networks,categories):
    output= "Description: "+description+"\n"+"Rules: "+rules+"\n"
    output1="severity: "+severity+"\n"
    output2="source_network: "+source_network+"\n"
    output3="destination_networks: "+destination_networks+"\n"
    output4="categories: "+categories

    return output+"\n"+output1+"\n"+output2+"\n"+output3+"\n"+output4




def get_epochdate ():
    final_datetime = datetime.now() - timedelta(minutes=40)
    return int(final_datetime.timestamp()*1000)