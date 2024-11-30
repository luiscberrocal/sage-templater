from tests.factories import SmallBoxRecordSchemaFactory


class TestSmallBoxRecordSchema:
    def test_create(self):
        schema = SmallBoxRecordSchemaFactory.create()
        assert schema
        print(schema)
