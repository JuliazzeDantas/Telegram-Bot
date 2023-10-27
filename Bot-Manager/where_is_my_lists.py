class MenuButton:
    def __init__(self):
        self.menu_button =  [ #list_of_commands tem que ser na forma: list= [{"command":"a", "description":"aaa"},{"command":"b","description":"bbb"}]
                    {"command":"help", "description":"Ajuda!"},
                    {"command":"comuns", "description":"Recheios Comuns"},
                    {"command":"gourmet", "description":"Recheios Gourmet"},
                    {"command":"bebida", "description":"Bebidas"},
                    {"command":"massa", "description":"Itens para A Massa"},
                    {"command":"funcionario", "description":"Funcionários"},
                    {"command":"estrutura", "description":"Gastos Estruturais"},
                    {"command":"manutencao", "description":"Manutenção de Equipamento"}
                ]

        self.list_of_command = [ #list_of_commands tem que ser na forma: list= [{"command":"a", "description":"aaa"},{"command":"b","description":"bbb"}]
                "/help", 
                "/comuns", 
                "/gourmet", 
                "/bebida", 
                "/massa", 
                "/estrutura",
                "/manutencao", 
            ]


class InlineKeyboard:
    def __init__(self):
        self.comun_product =  [
                    [{'text' : 'Mussarela', 'callback_data' : 'mussarela'},            {'text' : 'Calabresa', 'callback_data' : 'calabresa'},     {'text' : 'Frango', 'callback_data' : 'frango'}], 
                    [{'text' : 'Apresuntado', 'callback_data' : 'apresuntado'},        {'text' : 'Milho', 'callback_data' : 'milho'},             {'text' : 'Ervilha', 'callback_data' : 'ervilha'}],
                    [{'text' : 'Pimenta', 'callback_data' : 'pimenta'},                {'text' : 'Oregano', 'callback_data' : 'oregao'},          {'text' : 'Cebola', 'callback_data' : 'cebola'}],
                    [{'text' : 'Granulado', 'callback_data' : 'granulado'},            {'text' : 'Coco', 'callback_data' : 'coco'},               {'text' : 'M&Ms', 'callback_data' : 'mms'}],
                    [{'text' : 'Chocolate Preto', 'callback_data' : 'preto'},          {'text' : 'Chocolate Branco', 'callback_data' : 'branco'}, {'text' : 'Catupiry', 'callback_data' : 'catupiry'}],   
                ]


        self.gourmet_product = [
                    [{'text' : 'Bacon', 'callback_data' : 'bacon'},  {'text' : 'Carne Seca', 'callback_data' : 'carne'},  {'text' : 'Cheddar', 'callback_data' : 'cheddar'}], 
                    [{'text' : 'Atum', 'callback_data' : 'atum'},    {'text' : 'Brócolis', 'callback_data' : 'brocolis'}, {'text' : 'Alho', 'callback_data' : 'alho'}]
                ]


        self.drink_product =  [
                    [{'text' : 'Dolly Guarná', 'callback_data' : 'dollyg'}, {'text' : 'Dolly Laranja', 'callback_data' : 'dollylj'},     {'text' : 'Dolly Limão', 'callback_data' : 'dollylm'}], 
                    [{'text' : 'Coca 2L', 'callback_data' : 'coca2'},       {'text' : 'Coca Zero', 'callback_data' : 'cocazero'},        {'text' : 'Coca 1L', 'callback_data' : 'coca1'}],
                    [{'text' : 'Guaraná 2L', 'callback_data' : 'guarana2'}, {'text' : 'Guaraná 1L', 'callback_data' : 'guarana1'},       {'text' : 'Suco', 'callback_data' : 'suco'}],
                    [{'text' : 'Coca Lata', 'callback_data' : 'cocalata'},  {'text' : 'Guaraná Lata', 'callback_data' : 'guaranalata'},  {'text' : 'Água 500mL', 'callback_data' : 'agua'}],
                    [{'text' : 'Skol', 'callback_data' : 'skol'},           {'text' : 'Brahma Duplo Malte', 'callback_data' : 'brahma'}]
                ]


        self.structure_list = [
                    [{'text' : 'Gás', 'callback_data' : 'gas'},{'text' : 'Luz', 'callback_data' : 'luz'},  {'text' : 'Água', 'callback_data' : 'agua'}]
                ]


        self.pizza_dough_list = [
                    [{'text' : 'Farinha', 'callback_data' : 'farinha'},  {'text' : 'Açucar', 'callback_data' : 'sal'},  {'text' : 'Fermento', 'callback_data' : 'fermento'}], 
                    [{'text' : 'Açucar', 'callback_data' : 'acucar'},    {'text' : 'Molho', 'callback_data' : 'molho'}, {'text' : 'Caixa', 'callback_data' : 'caixa'}]
                ]