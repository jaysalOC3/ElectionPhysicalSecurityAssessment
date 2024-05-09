import random

def list_return_threats():
    nodes = [
        {"name": "Reconnaissance"},
        {"name": "Resource Development"},
        {"name": "Initial Access"},
        {"name": "Execution"},
        {"name": "Persistence"},
        {"name": "Privilege Escalation"},
        {"name": "Defense Evasion"},
        {"name": "Credential Access"},
        {"name": "Discovery"},
        {"name": "Lateral Movement"},
        {"name": "Collection"},
        {"name": "Command and Control"},
        {"name": "Exfiltration"},
        {"name": "Impact"},
    ]
    return nodes

def list_return_treatments():
    nodes = [
        {"name": "Mitigated"},
        {"name": "Partially Mitigated"},
        {"name": "Accepted"},
        {"name": "Unmitigated"},
    ]
    return nodes

def list_return_products():
    nodes = [
        {"name": "Product 1"},
        {"name": "Product 2"},
        {"name": "Product 3"},
        {"name": "Product 4"},
    ]
    return nodes

def generate_product_threats():
    return_links = []
    assigned_threats = set()

    for product in list_return_products():
        threats = list_return_threats()
        for threat_num in range(3):
            if threats:
                selected_item = random.choice(threats)
                threats.remove(selected_item)
                assigned_threats.add(selected_item["name"])
                return_links.append({"source": selected_item["name"], "target": product["name"], "value": 3})
        return_links.append({"source": product["name"], "target": "Mitigated", "value": 3})

    unassigned_threats = set(threat["name"] for threat in list_return_threats()) - assigned_threats
    for threat in unassigned_threats:
        target = random.choice(["Partially Mitigated", "Accepted", "Unmitigated"])
        return_links.append({"source": threat, "target": target, "value": 3})

    print(return_links)
    return return_links

def generate_risk_landscape_data():
    # Business logic to generate the data dynamically
    # This can involve querying the database, performing calculations, etc.
    nodes = []
    nodes += list_return_threats()
    nodes += list_return_treatments()
    nodes += list_return_products()

    links = generate_product_threats()

    data = {
        "nodes": nodes,
        "links": links
    }

    return data