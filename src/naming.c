// ❌ BAD: Variable and function names not in snake_case
int RdSample()
{                         // Function name should be snake_case: read_sample()
    int bufferSize = 100; // Variable should be snake_case: buffer_size
    return bufferSize;
}

// ✅ GOOD:
int read_sample()
{
    int buffer_size = 100;
    return buffer_size;
}
