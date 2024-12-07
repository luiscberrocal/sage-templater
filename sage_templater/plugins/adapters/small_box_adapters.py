
from sage_templater.schemas import SmallBoxRecordSchema, SmallBoxSageRecordSchema


def export_small_box_sage_record(record: SmallBoxRecordSchema, reference: str) -> SmallBoxSageRecordSchema:
    """Export a small box record to a Sage record."""
    description = (f"{record.name} ruc {record.national_id} dv {record.verification_digit} "
                   f"fact: {record.invoice} {record.description}")
    return SmallBoxSageRecordSchema(
        date=record.date,
        reference=reference,
        description=description,
        amount=record.total,
        account="",
        distribution_number=1,
    )
