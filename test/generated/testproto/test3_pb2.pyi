"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class OuterEnum(_OuterEnum, metaclass=_OuterEnumEnumTypeWrapper):
    pass
class _OuterEnum:
    V = typing.NewType('V', builtins.int)
class _OuterEnumEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_OuterEnum.V], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    UNKNOWN = OuterEnum.V(0)
    FOO3 = OuterEnum.V(1)
    BAR3 = OuterEnum.V(2)

UNKNOWN = OuterEnum.V(0)
FOO3 = OuterEnum.V(1)
BAR3 = OuterEnum.V(2)
global___OuterEnum = OuterEnum


class OuterMessage3(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    A_STRING_FIELD_NUMBER: builtins.int
    a_string: typing.Text = ...
    def __init__(self,
        *,
        a_string : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["a_string",b"a_string"]) -> None: ...
global___OuterMessage3 = OuterMessage3

class SimpleProto3(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class InnerEnum(_InnerEnum, metaclass=_InnerEnumEnumTypeWrapper):
        pass
    class _InnerEnum:
        V = typing.NewType('V', builtins.int)
    class _InnerEnumEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_InnerEnum.V], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        INNER1 = SimpleProto3.InnerEnum.V(0)
        INNER2 = SimpleProto3.InnerEnum.V(1)

    INNER1 = SimpleProto3.InnerEnum.V(0)
    INNER2 = SimpleProto3.InnerEnum.V(1)

    class MapScalarEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int = ...
        value: typing.Text = ...
        def __init__(self,
            *,
            key : builtins.int = ...,
            value : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    class MapMessageEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.int = ...
        @property
        def value(self) -> global___OuterMessage3: ...
        def __init__(self,
            *,
            key : builtins.int = ...,
            value : typing.Optional[global___OuterMessage3] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...

    A_STRING_FIELD_NUMBER: builtins.int
    A_REPEATED_STRING_FIELD_NUMBER: builtins.int
    A_OUTER_ENUM_FIELD_NUMBER: builtins.int
    OUTER_MESSAGE_FIELD_NUMBER: builtins.int
    INNER_ENUM_FIELD_NUMBER: builtins.int
    A_ONEOF_1_FIELD_NUMBER: builtins.int
    A_ONEOF_2_FIELD_NUMBER: builtins.int
    OUTER_MESSAGE_IN_ONEOF_FIELD_NUMBER: builtins.int
    OUTER_ENUM_IN_ONEOF_FIELD_NUMBER: builtins.int
    INNER_ENUM_IN_ONEOF_FIELD_NUMBER: builtins.int
    B_ONEOF_1_FIELD_NUMBER: builtins.int
    B_ONEOF_2_FIELD_NUMBER: builtins.int
    BOOL_FIELD_NUMBER: builtins.int
    OUTERENUM_FIELD_NUMBER: builtins.int
    OUTERMESSAGE3_FIELD_NUMBER: builtins.int
    MAP_SCALAR_FIELD_NUMBER: builtins.int
    MAP_MESSAGE_FIELD_NUMBER: builtins.int
    AN_OPTIONAL_STRING_FIELD_NUMBER: builtins.int
    a_string: typing.Text = ...
    @property
    def a_repeated_string(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    a_outer_enum: global___OuterEnum.V = ...
    @property
    def outer_message(self) -> global___OuterMessage3: ...
    inner_enum: global___SimpleProto3.InnerEnum.V = ...
    a_oneof_1: typing.Text = ...
    a_oneof_2: typing.Text = ...
    @property
    def outer_message_in_oneof(self) -> global___OuterMessage3: ...
    outer_enum_in_oneof: global___OuterEnum.V = ...
    inner_enum_in_oneof: global___SimpleProto3.InnerEnum.V = ...
    b_oneof_1: typing.Text = ...
    b_oneof_2: typing.Text = ...
    @property
    def bool(self) -> global___OuterMessage3: ...
    OuterEnum: global___OuterEnum.V = ...
    """Test having fieldname match messagename"""

    @property
    def OuterMessage3(self) -> global___OuterMessage3: ...
    @property
    def map_scalar(self) -> google.protobuf.internal.containers.ScalarMap[builtins.int, typing.Text]:
        """Test generation of map"""
        pass
    @property
    def map_message(self) -> google.protobuf.internal.containers.MessageMap[builtins.int, global___OuterMessage3]: ...
    an_optional_string: typing.Text = ...
    def __init__(self,
        *,
        a_string : typing.Text = ...,
        a_repeated_string : typing.Optional[typing.Iterable[typing.Text]] = ...,
        a_outer_enum : global___OuterEnum.V = ...,
        outer_message : typing.Optional[global___OuterMessage3] = ...,
        inner_enum : global___SimpleProto3.InnerEnum.V = ...,
        a_oneof_1 : typing.Text = ...,
        a_oneof_2 : typing.Text = ...,
        outer_message_in_oneof : typing.Optional[global___OuterMessage3] = ...,
        outer_enum_in_oneof : global___OuterEnum.V = ...,
        inner_enum_in_oneof : global___SimpleProto3.InnerEnum.V = ...,
        b_oneof_1 : typing.Text = ...,
        b_oneof_2 : typing.Text = ...,
        bool : typing.Optional[global___OuterMessage3] = ...,
        OuterEnum : global___OuterEnum.V = ...,
        OuterMessage3 : typing.Optional[global___OuterMessage3] = ...,
        map_scalar : typing.Optional[typing.Mapping[builtins.int, typing.Text]] = ...,
        map_message : typing.Optional[typing.Mapping[builtins.int, global___OuterMessage3]] = ...,
        an_optional_string : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["OuterMessage3",b"OuterMessage3","_an_optional_string",b"_an_optional_string","a_oneof",b"a_oneof","a_oneof_1",b"a_oneof_1","a_oneof_2",b"a_oneof_2","an_optional_string",b"an_optional_string","b_oneof",b"b_oneof","b_oneof_1",b"b_oneof_1","b_oneof_2",b"b_oneof_2","bool",b"bool","inner_enum_in_oneof",b"inner_enum_in_oneof","outer_enum_in_oneof",b"outer_enum_in_oneof","outer_message",b"outer_message","outer_message_in_oneof",b"outer_message_in_oneof"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["OuterEnum",b"OuterEnum","OuterMessage3",b"OuterMessage3","_an_optional_string",b"_an_optional_string","a_oneof",b"a_oneof","a_oneof_1",b"a_oneof_1","a_oneof_2",b"a_oneof_2","a_outer_enum",b"a_outer_enum","a_repeated_string",b"a_repeated_string","a_string",b"a_string","an_optional_string",b"an_optional_string","b_oneof",b"b_oneof","b_oneof_1",b"b_oneof_1","b_oneof_2",b"b_oneof_2","bool",b"bool","inner_enum",b"inner_enum","inner_enum_in_oneof",b"inner_enum_in_oneof","map_message",b"map_message","map_scalar",b"map_scalar","outer_enum_in_oneof",b"outer_enum_in_oneof","outer_message",b"outer_message","outer_message_in_oneof",b"outer_message_in_oneof"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_an_optional_string",b"_an_optional_string"]) -> typing.Optional[typing_extensions.Literal["an_optional_string"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["a_oneof",b"a_oneof"]) -> typing.Optional[typing_extensions.Literal["a_oneof_1","a_oneof_2","outer_message_in_oneof","outer_enum_in_oneof","inner_enum_in_oneof"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["b_oneof",b"b_oneof"]) -> typing.Optional[typing_extensions.Literal["b_oneof_1","b_oneof_2"]]: ...
global___SimpleProto3 = SimpleProto3
