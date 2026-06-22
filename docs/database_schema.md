```text
class User:
    id: uuid for identify user
    full_name:  name of the user
    phone_number: phone number of the user
    email: email of the user
    password_hash:  user password saved hased version
    date_of_birth: brithday of the user (maybe usefull for doctors)
    gender: gender(maybe usefull for doctors)
    role: role("paitent","doctor","admin")


class Conversation(Base):
    id : id
    user_id : foreign key from User id
    thread_id: for LLM
    title : for showing chat history 
    created_at : time 
    last_update : time 


class MessageHistory(Base):
    """ 
    - Here we save the conversation message  between ai and human 
    """
    id :  id 
    conversation_id: from conversation table 
    message : autal conversation of ai 
    sender_role : (ai,human)
    created_at : time 
```

## `**Initial goal :**`

### `1st Core Features:`
- The user uploads an image of a prescription.
- We extract the text from the image using OCR (Optical Character Recognition) and AI-based parsing.
- We apply a Human-in-the-Loop (HITL) process to verify and correct the extracted medicine names to ensure medical accuracy.
- We match the verified medicines with our internal drugs database (drugs_master) to normalize names and retrieve standard medical information.
- From the database, we collect relevant details for each medicine, including:
    - Side effects
    - Drug warnings
    - Standard dosage information
- We analyze the combination of prescribed medicines to detect possible drug-drug interactions.
- If any risk or unsafe combination is detected, the system generates an interaction alert for review or immediate action.


