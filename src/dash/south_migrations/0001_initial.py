# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

# Safe User import for Django < 1.5
try:
    from django.contrib.auth import get_user_model
except ImportError:
    from django.contrib.auth.models import User
else:
    User = get_user_model()

# With the default User model these will be 'auth.User' and 'auth.user'
# so instead of using orm['auth.User'] we can use orm[user_orm_label]
user_orm_label = '%s.%s' % (User._meta.app_label, User._meta.object_name)
user_model_label = '%s.%s' % (User._meta.app_label, User._meta.module_name)

class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DashboardSettings'
        db.create_table(u'dash_dashboardsettings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm[user_orm_label], unique=True)),
            ('layout_uid', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('is_public', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'dash', ['DashboardSettings'])

        # Adding model 'DashboardWorkspace'
        db.create_table(u'dash_dashboardworkspace', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm[user_orm_label])),
            ('layout_uid', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from='name', unique_with=())),
            ('position', self.gf('dash.fields.OrderField')(null=True, blank=True)),
            ('is_public', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'dash', ['DashboardWorkspace'])

        # Adding unique constraint on 'DashboardWorkspace', fields ['user', 'slug']
        db.create_unique(u'dash_dashboardworkspace', ['user_id', 'slug'])

        # Adding unique constraint on 'DashboardWorkspace', fields ['user', 'name']
        db.create_unique(u'dash_dashboardworkspace', ['user_id', 'name'])

        # Adding model 'DashboardEntry'
        db.create_table(u'dash_dashboardentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm[user_orm_label])),
            ('workspace', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dash.DashboardWorkspace'], null=True, blank=True)),
            ('layout_uid', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('placeholder_uid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('plugin_uid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('plugin_data', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('position', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'dash', ['DashboardEntry'])

        # Adding model 'DashboardPlugin'
        db.create_table(u'dash_dashboardplugin', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plugin_uid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'dash', ['DashboardPlugin'])

        # Adding M2M table for field users on 'DashboardPlugin'
        m2m_table_name = db.shorten_name(u'dash_dashboardplugin_users')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('dashboardplugin', models.ForeignKey(orm[u'dash.dashboardplugin'], null=False)),
            ('user', models.ForeignKey(orm[user_orm_label], null=False))
        ))
        db.create_unique(m2m_table_name, ['dashboardplugin_id', 'user_id'])

        # Adding M2M table for field groups on 'DashboardPlugin'
        m2m_table_name = db.shorten_name(u'dash_dashboardplugin_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('dashboardplugin', models.ForeignKey(orm[u'dash.dashboardplugin'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['dashboardplugin_id', 'group_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'DashboardWorkspace', fields ['user', 'name']
        db.delete_unique(u'dash_dashboardworkspace', ['user_id', 'name'])

        # Removing unique constraint on 'DashboardWorkspace', fields ['user', 'slug']
        db.delete_unique(u'dash_dashboardworkspace', ['user_id', 'slug'])

        # Deleting model 'DashboardSettings'
        db.delete_table(u'dash_dashboardsettings')

        # Deleting model 'DashboardWorkspace'
        db.delete_table(u'dash_dashboardworkspace')

        # Deleting model 'DashboardEntry'
        db.delete_table(u'dash_dashboardentry')

        # Deleting model 'DashboardPlugin'
        db.delete_table(u'dash_dashboardplugin')

        # Removing M2M table for field users on 'DashboardPlugin'
        db.delete_table(db.shorten_name(u'dash_dashboardplugin_users'))

        # Removing M2M table for field groups on 'DashboardPlugin'
        db.delete_table(db.shorten_name(u'dash_dashboardplugin_groups'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        user_model_label: {
            'Meta': {'object_name': User.__name__, 'db_table': "'%s'" % User._meta.db_table},
            User._meta.pk.attname: ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'%s'" % User._meta.pk.column}),
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'dash.dashboardentry': {
            'Meta': {'object_name': 'DashboardEntry'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'layout_uid': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'placeholder_uid': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'plugin_data': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'plugin_uid': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm[user_orm_label]"}),
            'workspace': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dash.DashboardWorkspace']", 'null': 'True', 'blank': 'True'})
        },
        u'dash.dashboardplugin': {
            'Meta': {'object_name': 'DashboardPlugin'},
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['auth.Group']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plugin_uid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm[user_orm_label]", 'null': 'True', 'blank': 'True'})
        },
        u'dash.dashboardsettings': {
            'Meta': {'object_name': 'DashboardSettings'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'layout_uid': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm[user_orm_label]", 'unique': 'True'})
        },
        u'dash.dashboardworkspace': {
            'Meta': {'unique_together': "(('user', 'slug'), ('user', 'name'))", 'object_name': 'DashboardWorkspace'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'layout_uid': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'position': ('dash.fields.OrderField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'name'", 'unique_with': '()'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm[user_orm_label]"})
        }
    }

    complete_apps = ['dash']
