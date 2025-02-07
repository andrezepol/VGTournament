import json

def lambda_handler(event, context):
    body = json.loads(event.get("body", "{}"))

    # Aquí iría la lógica para crear el usuario
    response = {
        "statusCode": 201,
        "body": json.dumps({"message": "Usuario creado con éxito", "user": body})
    }

    return response
