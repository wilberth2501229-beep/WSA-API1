from supabase import create_client

def inicializar_db():
    cliente = create_client( "https://rhutyprqlktipdchmqvp.supabase.co" , 'sb_publishable_cgajE7vC7Mt2xBOJBaO1IA_uDYM6yvl')
    return cliente
