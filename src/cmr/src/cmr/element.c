#include <cmr/element.h>

#include <stdio.h>
#include <string.h>

static char elementStringBuffer[32];

CMR_EXPORT
const char* CMRelementString(CMR_ELEMENT element, char* buffer)
{
  if (!buffer)
    buffer = elementStringBuffer;

  if (element < 0)
    sprintf(buffer, "r%d", -element);
  else if (element > 0)
    sprintf(buffer, "c%d", element);
  else
    strcpy(buffer, "<invalid element>");
  return buffer;
}
