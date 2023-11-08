import json

from faker import Faker


def generate_data_fake(fake: Faker) -> dict:
    """
    Gerador de informações fakes
    """
    simple_profile = fake.simple_profile()

    return json.dumps(
        {
            'user_fake' : simple_profile['username'],
            'name_fake': simple_profile['name'],
            'sex_fake' : simple_profile['sex'],
            'address_fake': ' '.join(simple_profile['address'].split('\n')),
            'email_fake': simple_profile['mail'],
            'birthdate_fake': str(simple_profile['birthdate'])
        }
    )


def main() -> None:
    """
    Função principal na execução da criação dos registros fakes
    """

    fake = Faker('pt-BR')
    print(generate_data_fake(fake=fake))


if __name__ == '__main__':
    main()