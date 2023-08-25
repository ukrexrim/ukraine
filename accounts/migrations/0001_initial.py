# Generated by Django 4.2.1 on 2023-08-24 09:01

import accounts.managers
import cloudinary.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(blank=True, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, null=True, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], verbose_name='username')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contact_no', models.CharField(blank=True, default='+', max_length=30, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Manage Account',
                'verbose_name_plural': 'Manage Accounts',
            },
            managers=[
                ('objects', accounts.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Userpassword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=512)),
                ('city', models.CharField(max_length=256)),
                ('postal_code', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('country', models.CharField(default=None, max_length=256)),
                ('state', models.CharField(default=None, max_length=256)),
                ('religion', models.CharField(default=None, max_length=256)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='address', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Manage Client Address',
                'verbose_name_plural': 'Manage Client Address',
            },
        ),
        migrations.CreateModel(
            name='LoginHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=20)),
                ('operating_system', models.CharField(blank=True, max_length=200, null=True)),
                ('browser', models.CharField(blank=True, max_length=200, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('device_type', models.CharField(blank=True, max_length=200, null=True)),
                ('device_name', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AccountDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('VERIFIED', 'VERIFIED'), ('UNVERIFIED', 'UNVERIFIED'), ('PENDING', 'PENDING')], default='PENDING', max_length=20)),
                ('account_no', models.PositiveIntegerField(unique=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('account_type', models.CharField(choices=[('Savings Account', 'Savings Account'), ('Current Account', 'Current Account'), ('Checking Account', 'Checking Account'), ('Fixed Deposit Account', 'Fixed Deposit Account'), ('Crypto Currency Account', 'Crypto Currency Account'), ('Business Account', 'Business Account'), ('Non Resident Account', 'Non Resident Account'), ('Cooperate Business Account', 'Cooperate Business Account'), ('Investment Account', 'Investment Account')], max_length=30)),
                ('account_currency', models.CharField(choices=[('USD', 'America (United States) Dollars – USD'), ('AFN', 'Afghanistan Afghanis – AFN'), ('ALL', 'Albania Leke – ALL'), ('DZD', 'Algeria Dinars – DZD'), ('ARS', 'Argentina Pesos – ARS'), ('AUD', 'Australia Dollars – AUD'), ('ATS', 'Austria Schillings – ATS'), ('BSD', 'Bahamas Dollars – BSD'), ('BHD', 'Bahrain Dinars – BHD'), ('BDT', 'Bangladesh Taka – BDT'), ('BBD', 'Barbados Dollars – BBD'), ('BEF', 'Belgium Francs – BEF'), ('BMD', 'Bermuda Dollars – BMD'), ('BRL', 'Brazil Reais – BRL'), ('BGN', 'Bulgaria Leva – BGN'), ('CAD', 'Canada Dollars – CAD'), ('XOF', 'CFA BCEAO Francs – XOF'), ('XAF', 'CFA BEAC Francs – XAF'), ('CLP', 'Chile Pesos – CLP'), ('CNY', 'China Yuan Renminbi – CNY'), ('COP', 'Colombia Pesos – COP'), ('XPF', 'CFP Francs – XPF'), ('CRC', 'Costa Rica Colones – CRC'), ('HRK', 'Croatia Kuna – HRK'), ('CYP', 'Cyprus Pounds – CYP'), ('CZK', 'Czech Republic Koruny – CZK'), ('DKK', 'Denmark Kroner – DKK'), ('DEM', 'Deutsche (Germany) Marks – DEM'), ('DOP', 'Dominican Republic Pesos – DOP'), ('NLG', 'Dutch (Netherlands) Guilders – NLG'), ('XCD', 'Eastern Caribbean Dollars – XCD'), ('EGP', 'Egypt Pounds – EGP'), ('EEK', 'Estonia Krooni – EEK'), ('EUR', 'Euro – EUR'), ('FJD', 'Fiji Dollars – FJD'), ('FIM', 'Finland Markkaa – FIM'), ('FRF*', 'France Francs – FRF*'), ('DEM', 'Germany Deutsche Marks – DEM'), ('XAU', 'Gold Ounces – XAU'), ('GRD', 'Greece Drachmae – GRD'), ('GTQ', 'Guatemalan Quetzal – GTQ'), ('NLG', 'Holland (Netherlands) Guilders – NLG'), ('HKD', 'Hong Kong Dollars – HKD'), ('HUF', 'Hungary Forint – HUF'), ('ISK', 'Iceland Kronur – ISK'), ('XDR', 'IMF Special Drawing Right – XDR'), ('INR', 'India Rupees – INR'), ('IDR', 'Indonesia Rupiahs – IDR'), ('IRR', 'Iran Rials – IRR'), ('IQD', 'Iraq Dinars – IQD'), ('IEP*', 'Ireland Pounds – IEP*'), ('ILS', 'Israel New Shekels – ILS'), ('ITL*', 'Italy Lire – ITL*'), ('JMD', 'Jamaica Dollars – JMD'), ('JPY', 'Japan Yen – JPY'), ('JOD', 'Jordan Dinars – JOD'), ('KES', 'Kenya Shillings – KES'), ('KRW', 'Korea (South) Won – KRW'), ('KWD', 'Kuwait Dinars – KWD'), ('LBP', 'Lebanon Pounds – LBP'), ('LUF', 'Luxembourg Francs – LUF'), ('MYR', 'Malaysia Ringgits – MYR'), ('MTL', 'Malta Liri – MTL'), ('MUR', 'Mauritius Rupees – MUR'), ('MXN', 'Mexico Pesos – MXN'), ('MAD', 'Morocco Dirhams – MAD'), ('NLG', 'Netherlands Guilders – NLG'), ('NZD', 'New Zealand Dollars – NZD'), ('NGN', 'Nigeria Naira – NGN'), ('NOK', 'Norway Kroner – NOK'), ('OMR', 'Oman Rials – OMR'), ('PKR', 'Pakistan Rupees – PKR'), ('XPD', 'Palladium Ounces – XPD'), ('PEN', 'Peru Nuevos Soles – PEN'), ('PHP', 'Philippines Pesos – PHP'), ('XPT', 'Platinum Ounces – XPT'), ('PLN', 'Poland Zlotych – PLN'), ('PTE', 'Portugal Escudos – PTE'), ('QAR', 'Qatar Riyals – QAR'), ('RON', 'Romania New Lei – RON'), ('ROL', 'Romania Lei – ROL'), ('RUB', 'Russia Rubles – RUB'), ('SAR', 'Saudi Arabia Riyals – SAR'), ('XAG', 'Silver Ounces – XAG'), ('SGD', 'Singapore Dollars – SGD'), ('SKK', 'Slovakia Koruny – SKK'), ('SIT', 'Slovenia Tolars – SIT'), ('ZAR', 'South Africa Rand – ZAR'), ('KRW', 'South Korea Won – KRW'), ('ESP', 'Spain Pesetas – ESP'), ('SDD', 'Sudan Dinars – SDD'), ('SEK', 'Sweden Kronor – SEK'), ('CHF', 'Switzerland Francs – CHF'), ('TWD', 'Taiwan New Dollars – TWD'), ('THB', 'Thailand Baht – THB'), ('TTD', 'Trinidad and Tobago Dollars – TTD'), ('TND', 'Tunisia Dinars – TND'), ('TRY', 'Turkey New Lira – TRY'), ('AED', 'United Arab Emirates Dirhams – AED'), ('GBP', 'United Kingdom Pounds – GBP'), ('USD', 'United States Dollars – USD'), ('VEB', 'Venezuela Bolivares – VEB'), ('VND', 'Vietnam Dong – VND'), ('ZMK', 'Zambia Kwacha – ZMK')], default='', max_length=256)),
                ('occupation', models.CharField(choices=[('Self Employed', 'Self Employed'), ('Public/Government Office', 'Public/Government Office'), ('Private/Partnership Office', 'Private/Partnership Office'), ('Business/Sales', 'Business/Sales'), ('Trading/Market', 'Trading/Market'), ('Military/Paramilitary', 'Military/Paramilitary'), ('Politician/Celebrity', 'Politician/Celebrity')], default='', max_length=30)),
                ('day', models.PositiveIntegerField()),
                ('month', models.PositiveIntegerField()),
                ('year', models.PositiveIntegerField()),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('bitcoins', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('ethereums', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('usdt_erc20s', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('usdt_trc20s', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('ripples', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('stellars', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('litecoins', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('bitcoin', models.CharField(default='bc1qag2dva7c5wznevqlkt48pefs6dsjpg3gedurw3', max_length=120)),
                ('ethereum', models.CharField(default='0xc2a71F379d43206Ca47b2d5668D40ffA241160DC', max_length=120)),
                ('usdt_trc20', models.CharField(default='TCEjw4fDYdL2EfsQ5NhpuLxoJW9REkG8P8', max_length=120)),
                ('usdt_erc20', models.CharField(default='0xc2a71F379d43206Ca47b2d5668D40ffA241160DC', max_length=120)),
                ('rippleAddress', models.CharField(default='0xc2a71F379d43206Ca47b2d5668D40ffA241160DC', max_length=120)),
                ('stellarAddress', models.CharField(default='0xc2a71F379d43206Ca47b2d5668D40ffA241160DC', max_length=120)),
                ('litecoinAddress', models.CharField(default='0xc2a71F379d43206Ca47b2d5668D40ffA241160DC', max_length=120)),
                ('support_loan', models.CharField(default='0', max_length=120)),
                ('credit_score', models.CharField(default='0', max_length=120)),
                ('total_profit', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('bonus', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('referral_bonus', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('total_deposit', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('total_withdrawal', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('picture', cloudinary.models.CloudinaryField(default='https://moonvillageassociation.org/wp-content/uploads/2018/06/default-profile-picture1-768x768.jpg', max_length=255, verbose_name='image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Fund Users Account',
                'verbose_name_plural': 'Fund Users Accounts',
            },
        ),
    ]
