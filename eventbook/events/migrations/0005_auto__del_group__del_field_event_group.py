# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Group'
        db.delete_table(u'events_group')

        # Deleting field 'Event.group'
        db.delete_column(u'events_event', 'group_id')


    def backwards(self, orm):
        # Adding model 'Group'
        db.create_table(u'events_group', (
            ('numMembers', self.gf('django.db.models.fields.IntegerField')(default=0)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('private', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=75, unique=True)),
        ))
        db.send_create_signal(u'events', ['Group'])

        # Adding field 'Event.group'
        db.add_column(u'events_event', 'group',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Group'], null=True),
                      keep_default=False)


    models = {
        u'events.event': {
            'Meta': {'object_name': 'Event'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 7, 29, 0, 0)'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['events']