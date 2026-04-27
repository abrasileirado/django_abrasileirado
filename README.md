# django-abrasileirado

Aplicação Django com campos específicos para o contexto brasileiro
(CPF, CNPJ, CEP, UF, Município, etc).

## Descrição

O **django-abrasileirado** fornece campos, formulários, validadores e mixins
para facilitar o uso de dados brasileiros em projetos Django, como CPF, CNPJ,
CEP, UF e Município, além de helpers para formulários e modelos.

## Instalação

1. Instale o pacote (exemplo para uso local):

```bash
pip install -e .
```

1. Adicione `django_brfied` ao seu `INSTALLED_APPS` no `settings.py` do seu
   projeto Django:

```python
INSTALLED_APPS = [
 ...
 'django_abrasileirado',
]
```

## Uso Básico

Exemplo de uso de campos em um modelo:

```python
from django_abrasileirado.models import CPFField, CNPJField, CEPField
from django_abrasileirado.models import UFField, MunicipioField


class Pessoa(models.Model):
    cpf = CPFField()
    cnpj = CNPJField()
    cep = CEPField()
    uf = UFField()
    municipio = MunicipioField()
```

> Why I create abrasileirado? Because **this is Brazil** (Toretto, 2020).

## Data types

* 🚫 Sim/Não (Enum)
* 🚫 Estado Civil (Enum) - Instituto Brasileiro de Geografia e Estatística (IBGE)
* 🚫 Cor/Raça (Enum) - IBGE
* 🚫 Sexo (Enum) - IBGE
* 🚫 Gênero (Enum) - IBGE*
* 🚫 Deficiência (Enum) - IBGE
* 🚫 Zona de habitação (Enum) - IBGE
* 🚫 Região geopolítica (Enum) - IBGE
* 🚫 Unidade federativa (Enum) - IBGE
* 🚫 CEP - Código de Endereçamento Postal - Empresa de Correio e Telegráfos (ECT)
* 🚫 CNES - Cadastro Nacional de Estabelecimento de Saúde - DATASUS
* 🚫 CNS - Cadastro Nacional de Saúde (Cartão SUS) - DATASUS
* 🚫 CPF - Cadastro de Pessoa Física - Receita Federal do Brasil (RFB)
* 🚫 CNPJ - Cadastro Nacional de Pessoa Jurídica - RFB
* 🚫 Modulo11
* 🚫 ProtocoloIntegrado
* 🚫 ProtocoloJustica
* 🚫 PJE
* 🚫 Boleto
* 🚫 NFE
* 🚫 Município

## Licença

[MIT](LICENSE). Veja o arquivo LICENSE.md para mais detalhes.

## Autor

Kelson da Costa Medeiros (<kelsoncm@gmail.com>)
