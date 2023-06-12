from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    try:
        import ensight
    except ImportError:
        from ansys.pyensight import ensight_api


class Support:
    """The ensight.utils.support interface

    This object provides a collection of general utility functions and objects.
    They can be used to simplify various issues that come up when using EnSight
    and PyEnSight.

    This class is instantiated as ``ensight.utils.support`` within EnSight Python
    and as ``Session.ensight.utils.support`` in PyEnSight.  The constructor is
    passed the interface which serves as the "ensight" module for either
    case.  As a result, the methods can be accessed as: ``ensight.utils.support.*``
    in EnSight Python or ``session.ensight.utils.support.*`` within PyEnSight.

    Args:
        interface:
            An entity that provides the 'ensight' namespace.  In the case
            of PyEnSight, ``Session.ensight`` is passed and in the case of
            EnSight Python, the ``ensight`` module is passed.
    """

    def __init__(self, interface: Union["ensight_api.ensight", "ensight"]):
        self._ensight = interface

    class ScopedName:
        """Allow for the use of 'with' to shorten APIs

        In the ensight and pyensight APIs, the interfaces can become lengthy.
        This class makes it possible to shorten APIs for modules, classes,
        namespaces, etc.

        Examples:

            ::

                sn = s.ensight.utils.support.ScopedName
                with sn(s.ensight.objs.core) as core, sn(s.ensight.objs.enums) as enums:
                    print(core.PARTS.find(True, enums.VISIBLE))


            ::

                sn = ensight.utils.support.ScopedName
                with sn(ensight.objs.core) as core, sn(ensight.objs.enums) as enums:
                    print(core.PARTS.find(True, enums.VISIBLE))


        """

        def __init__(self, obj: Any):
            self._obj = obj

        def __enter__(self) -> Any:
            return self._obj

        def __exit__(self, exc_type, exc_value, exc_trace):
            pass
