import csv

from apps.banks.models import Bank, Branch


def create_bank_and_branch():
    with open('utils/resources/bank_branches.csv', 'r') as file:
        reader = csv.DictReader(file)
        count = 0

        for row in reader:
            if count > 8000:
                break
            try:
                bank = Bank.objects.get(id=row['bank_id'])
                branch = Branch.objects.get(ifsc=row['ifsc'], bank=bank)

            except Branch.DoesNotExist:
                Branch.objects.create(bank=bank, ifsc=row['ifsc'], branch=row['branch'], address=row['address'],
                                      city=row['city'], district=row['district'], state=['state'])
                count += 1

            except Bank.DoesNotExist:
                bank = Bank.objects.create(id=row['bank_id'], name=row['bank_name'])
                Branch.objects.create(bank=bank, ifsc=row['ifsc'], branch=row['branch'], address=row['address'],
                                      city=row['city'], district=row['district'], state=['state'])
                count += 2
