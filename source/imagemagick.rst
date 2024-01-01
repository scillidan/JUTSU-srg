ImageMagick
===========

.. option:: dither

	``magick convert %1 -ordered-dither h4x4o -colors 8 _%1``

.. option:: gray_dither

	``magick convert %1 -colorspace Gray -ordered-dither o2x2 _%1``

.. option:: paint

	``magick convert %1 -paint 3 _%1``

.. option:: sketch

	``magick convert %1 -colorspace gray -sketch 0x10+120 _%1``

.. option:: charcoal

	``magick convert %1 -charcoal 2 _%1``

.. option:: border

	``magick convert %1 -bordercolor %3 -border %2 _%1``

====
Note
====

#. ``-auto-orient``

=========
Reference
=========

#. https://www.imagemagick.org