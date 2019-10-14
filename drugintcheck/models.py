# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Hersteller(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    hersteller = models.CharField(db_column='Hersteller', max_length=108, blank=True, null=True)  # Field name made lowercase.
    postleitzahl = models.CharField(db_column='Postleitzahl', max_length=9, blank=True, null=True)  # Field name made lowercase.
    stadt = models.CharField(db_column='Stadt', max_length=38, blank=True, null=True)  # Field name made lowercase.
    straße_und_hausnummer = models.CharField(db_column='Straße und Hausnummer', verbose_name='Straße und Hausnummer', max_length=42, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'hersteller'


class Interaktionen(models.Model):
    interactionclassid1 = models.ForeignKey('Interaktionsklassen', models.DO_NOTHING, db_column='INTERACTIONCLASSID1', related_name='interaction_one', primary_key=True, unique=False)  # Field name made lowercase.
    interactionclassid2 = models.ForeignKey('Interaktionsklassen', models.DO_NOTHING, db_column='INTERACTIONCLASSID2', related_name='interaction_two')  # Field name made lowercase.
    severity = models.CharField(db_column='SEVERITY', max_length=13, blank=True, null=True)  # Field name made lowercase.
    likelihood = models.CharField(db_column='LIKELIHOOD', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'interaktionen'
        unique_together = (('interactionclassid1', 'interactionclassid2'),)


class Interaktionsklassen(models.Model):
    interactionclassid = models.IntegerField(db_column='INTERACTIONCLASSID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=113, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'interaktionsklassen'


class Produkt(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    arzneimittel = models.CharField(db_column='Arzneimittel', max_length=150)  # Field name made lowercase.
    markteintrittsdatum = models.DateField(db_column='Markteintrittsdatum', blank=True, null=True)  # Field name made lowercase.
    hersteller = models.CharField(db_column='Hersteller', max_length=108, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'produkt'


class Produktinteraktionsklassen(models.Model):
    interactionclassid = models.ForeignKey('Interaktionsklassen', models.DO_NOTHING, db_column='INTERACTIONCLASSID', primary_key=True)  # Field name made lowercase.
    productid = models.ForeignKey('Produkt', models.DO_NOTHING, db_column='PRODUCTID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'produktinteraktionsklassen'
        unique_together = (('interactionclassid', 'productid'),)
