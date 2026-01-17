import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    

    #print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    #print(Passcard.objects.all())
    
    passcards = Passcard.objects.all()
    #print('owner_name: ', passcards[0].owner_name)
    #print('passcode: ', passcards[0].passcode)
    #print('created_at: ', passcards[0].created_at)
    #print('is_active: ', passcards[0].is_active)

    

    #active_passcards = []
    #for passcard in passcards:        
        #if passcard.is_active:
            #active_passcards.append(passcards)

    active_passcards = Passcard.objects.filter(is_active=True)

    print('Всего пропусков: ', len(passcards))
    print('Активных пропусков: ', len(active_passcards))