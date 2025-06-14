from pydantic import field_validator

from schemas.shared import PhoneNumberSchema, NonEmptyStringField


class VerifyPhoneNumberSchema(PhoneNumberSchema):
    otp: NonEmptyStringField(min_length=6, max_length=6)

    @field_validator('otp')
    @classmethod
    def otp_digits_only(cls, v: str) -> str:
        if not v.isdigit():
            raise ValueError("Otp must contain digits only")
        return v
