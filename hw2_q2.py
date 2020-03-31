from enum import Enum
from collections import namedtuple


Type = Enum("Type", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))

def meetup(agent_listing: tuple) -> list:
    """Model the outcome of the meetings of pairs of agents.

    The pairs of agents are ((a[0], a[1]), (a[2], a[3]), ...). If there's an uneven
    number of agents, the last agent will remain the same.

    Notes
    -----
    The rules governing the meetings were described in the question. The outgoing
    listing may change its internal ordering relative to the incoming one.

    Parameters
    ----------
    agent_listing : tuple of Agent
        A listing (tuple in this case) in which each element is of the Agent
        type, containing a 'name' field and a 'category' field, with 'category' being
        of the type Type.

    Returns
    -------
    updated_listing : list
        A list of Agents with their 'category' field changed according to the result
        of the meeting.
    """
    
    i=0
    updated_listing=[]
    one1val = 0
    two2val = 0
    one1=(-1)
    two2=(-1)
    for i in range (len(agent_listing)):
        if ((agent_listing[i].category.value ==5) or (agent_listing[i].category.value ==2)):
            updated_listing.append(agent_listing[i])
            if (i==((len(agent_listing))-1)) and (one1!=(-1)):
                updated_listing.append(agent_listing[one1])
            continue
        elif (one1==(-1)):
            one1=i
            one1val = agent_listing[one1].category.value
            if one1==((len(agent_listing))-1):
                updated_listing.append(agent_listing[one1])
            continue
        elif ((two2==(-1)) and (one1!=i)):
            two2=i
            two2val = agent_listing[two2].category.value
        if one1==((len(agent_listing))-1):
            updated_listing.append(agent_listing[one1])
            break
        if (one1val==1):
            if (two2val==1):
                updated_listing.append(agent_listing[one1])
                updated_listing.append(agent_listing[two2])
                one1=(-1)
                two2=(-1)
            else:
                two2val-=1
                updated_listing.append(agent_listing[one1])
                updated_listing.append(agent_listing[two2]._replace(category=Type(two2val)))
                one1=(-1)
                two2=(-1)
        elif (two2val==1):
            one1val-=1
            updated_listing.append(agent_listing[one1]._replace(category=Type(one1val)))
            updated_listing.append(agent_listing[two2])
            one1=(-1)
            two2=(-1)
        else:
            one1val+=1
            two2val+=1
            updated_listing.append(agent_listing[one1]._replace(category=Type(one1val)))
            updated_listing.append(agent_listing[two2]._replace(category=Type(two2val)))
            one1=(-1)
            two2=(-1)
        i+=1
    return (updated_listing)