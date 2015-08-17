# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Actor'
        db.create_table(u'engine_actor', (
            ('bid', self.gf('django.db.models.fields.AutoField')(max_length=255, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('role_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['engine.Role'])),
        ))
        db.send_create_signal(u'engine', ['Actor'])

        # Adding model 'Role'
        db.create_table(u'engine_role', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'engine', ['Role'])

        # Adding model 'Project'
        db.create_table(u'engine_project', (
            ('p_id', self.gf('django.db.models.fields.AutoField')(max_length=255, primary_key=True)),
            ('p_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('summary', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(default=None, related_name='children', null=True, blank=True, to=orm['engine.Project'])),
            ('project_leader', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pm', to=orm['engine.Actor'])),
            ('active_status', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')()),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'engine', ['Project'])

        # Adding M2M table for field actor on 'Project'
        m2m_table_name = db.shorten_name(u'engine_project_actor')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'engine.project'], null=False)),
            ('actor', models.ForeignKey(orm[u'engine.actor'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'actor_id'])

        # Adding model 'Task'
        db.create_table(u'engine_task', (
            ('tid', self.gf('django.db.models.fields.AutoField')(max_length=255, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['engine.Project'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('priority', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'engine', ['Task'])

        # Adding model 'MyProfile'
        db.create_table(u'engine_myprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mugshot', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('privacy', self.gf('django.db.models.fields.CharField')(default='registered', max_length=15)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='my_profile', unique=True, to=orm['auth.User'])),
            ('favourite_snack', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal(u'engine', ['MyProfile'])


    def backwards(self, orm):
        # Deleting model 'Actor'
        db.delete_table(u'engine_actor')

        # Deleting model 'Role'
        db.delete_table(u'engine_role')

        # Deleting model 'Project'
        db.delete_table(u'engine_project')

        # Removing M2M table for field actor on 'Project'
        db.delete_table(db.shorten_name(u'engine_project_actor'))

        # Deleting model 'Task'
        db.delete_table(u'engine_task')

        # Deleting model 'MyProfile'
        db.delete_table(u'engine_myprofile')


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
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'engine.actor': {
            'Meta': {'object_name': 'Actor'},
            'bid': ('django.db.models.fields.AutoField', [], {'max_length': '255', 'primary_key': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'role_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['engine.Role']"})
        },
        u'engine.myprofile': {
            'Meta': {'object_name': 'MyProfile'},
            'favourite_snack': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mugshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'privacy': ('django.db.models.fields.CharField', [], {'default': "'registered'", 'max_length': '15'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'my_profile'", 'unique': 'True', 'to': u"orm['auth.User']"})
        },
        u'engine.project': {
            'Meta': {'object_name': 'Project'},
            'active_status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'actor': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'actor_set'", 'symmetrical': 'False', 'to': u"orm['engine.Actor']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'p_id': ('django.db.models.fields.AutoField', [], {'max_length': '255', 'primary_key': 'True'}),
            'p_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'default': 'None', 'related_name': "'children'", 'null': 'True', 'blank': 'True', 'to': u"orm['engine.Project']"}),
            'project_leader': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pm'", 'to': u"orm['engine.Actor']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'engine.role': {
            'Meta': {'object_name': 'Role'},
            'department': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'engine.task': {
            'Meta': {'object_name': 'Task'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'priority': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['engine.Project']"}),
            'tid': ('django.db.models.fields.AutoField', [], {'max_length': '255', 'primary_key': 'True'})
        }
    }

    complete_apps = ['engine']