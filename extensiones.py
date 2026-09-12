import os

from dotenv import load_dotenv
from supabase import create_client


load_dotenv()

def inicializar_db():
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")

    if not supabase_url or not supabase_key:
        raise RuntimeError(
            "Configura SUPABASE_URL y SUPABASE_KEY en el archivo .env"
        )

    cliente = create_client(supabase_url, supabase_key)
    return cliente
