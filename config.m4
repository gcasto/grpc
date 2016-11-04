PHP_ARG_ENABLE(grpc, whether to enable grpc support,
[  --enable-grpc           Enable grpc support])

if test "$PHP_GRPC" != "no"; then
  dnl Write more examples of tests here...

  dnl # --with-grpc -> add include path
  PHP_ADD_INCLUDE(../../grpc/include)
  PHP_ADD_INCLUDE(../../grpc/src/php/ext/grpc)
  PHP_ADD_INCLUDE(../../grpc/third_party/boringssl/include)

  LIBS="-lpthread $LIBS"

  GRPC_SHARED_LIBADD="-lpthread $GRPC_SHARED_LIBADD"
  PHP_ADD_LIBRARY(pthread)

  PHP_ADD_LIBRARY(dl,,GRPC_SHARED_LIBADD)
  PHP_ADD_LIBRARY(dl)

  case $host in
    *darwin*) ;;
    *)
      PHP_ADD_LIBRARY(rt,,GRPC_SHARED_LIBADD)
      PHP_ADD_LIBRARY(rt)
      ;;
  esac

  PHP_NEW_EXTENSION(grpc,
    src/php/ext/grpc/byte_buffer.c \
    src/php/ext/grpc/call.c \
    src/php/ext/grpc/call_credentials.c \
    src/php/ext/grpc/channel.c \
    src/php/ext/grpc/channel_credentials.c \
    src/php/ext/grpc/completion_queue.c \
    src/php/ext/grpc/php_grpc.c \
    src/php/ext/grpc/server.c \
    src/php/ext/grpc/server_credentials.c \
    src/php/ext/grpc/timeval.c \
    src/core/lib/profiling/basic_timers.c \
    src/core/lib/profiling/stap_timers.c \
    src/core/lib/support/alloc.c \
    src/core/lib/support/avl.c \
    src/core/lib/support/backoff.c \
    src/core/lib/support/cmdline.c \
    src/core/lib/support/cpu_iphone.c \
    src/core/lib/support/cpu_linux.c \
    src/core/lib/support/cpu_posix.c \
    src/core/lib/support/cpu_windows.c \
    src/core/lib/support/env_linux.c \
    src/core/lib/support/env_posix.c \
    src/core/lib/support/env_windows.c \
    src/core/lib/support/histogram.c \
    src/core/lib/support/host_port.c \
    src/core/lib/support/log.c \
    src/core/lib/support/log_android.c \
    src/core/lib/support/log_linux.c \
    src/core/lib/support/log_posix.c \
    src/core/lib/support/log_windows.c \
    src/core/lib/support/mpscq.c \
    src/core/lib/support/murmur_hash.c \
    src/core/lib/support/percent_encoding.c \
    src/core/lib/support/slice.c \
    src/core/lib/support/slice_buffer.c \
    src/core/lib/support/stack_lockfree.c \
    src/core/lib/support/string.c \
    src/core/lib/support/string_posix.c \
    src/core/lib/support/string_util_windows.c \
    src/core/lib/support/string_windows.c \
    src/core/lib/support/subprocess_posix.c \
    src/core/lib/support/subprocess_windows.c \
    src/core/lib/support/sync.c \
    src/core/lib/support/sync_posix.c \
    src/core/lib/support/sync_windows.c \
    src/core/lib/support/thd.c \
    src/core/lib/support/thd_posix.c \
    src/core/lib/support/thd_windows.c \
    src/core/lib/support/time.c \
    src/core/lib/support/time_posix.c \
    src/core/lib/support/time_precise.c \
    src/core/lib/support/time_windows.c \
    src/core/lib/support/tls_pthread.c \
    src/core/lib/support/tmpfile_msys.c \
    src/core/lib/support/tmpfile_posix.c \
    src/core/lib/support/tmpfile_windows.c \
    src/core/lib/support/wrap_memcpy.c \
    src/core/lib/surface/init.c \
    src/core/lib/channel/channel_args.c \
    src/core/lib/channel/channel_stack.c \
    src/core/lib/channel/channel_stack_builder.c \
    src/core/lib/channel/compress_filter.c \
    src/core/lib/channel/connected_channel.c \
    src/core/lib/channel/deadline_filter.c \
    src/core/lib/channel/handshaker.c \
    src/core/lib/channel/http_client_filter.c \
    src/core/lib/channel/http_server_filter.c \
    src/core/lib/channel/message_size_filter.c \
    src/core/lib/compression/compression.c \
    src/core/lib/compression/message_compress.c \
    src/core/lib/debug/trace.c \
    src/core/lib/http/format_request.c \
    src/core/lib/http/httpcli.c \
    src/core/lib/http/parser.c \
    src/core/lib/iomgr/closure.c \
    src/core/lib/iomgr/combiner.c \
    src/core/lib/iomgr/endpoint.c \
    src/core/lib/iomgr/endpoint_pair_posix.c \
    src/core/lib/iomgr/endpoint_pair_uv.c \
    src/core/lib/iomgr/endpoint_pair_windows.c \
    src/core/lib/iomgr/error.c \
    src/core/lib/iomgr/ev_epoll_linux.c \
    src/core/lib/iomgr/ev_poll_and_epoll_posix.c \
    src/core/lib/iomgr/ev_poll_posix.c \
    src/core/lib/iomgr/ev_posix.c \
    src/core/lib/iomgr/exec_ctx.c \
    src/core/lib/iomgr/executor.c \
    src/core/lib/iomgr/iocp_windows.c \
    src/core/lib/iomgr/iomgr.c \
    src/core/lib/iomgr/iomgr_posix.c \
    src/core/lib/iomgr/iomgr_uv.c \
    src/core/lib/iomgr/iomgr_windows.c \
    src/core/lib/iomgr/load_file.c \
    src/core/lib/iomgr/network_status_tracker.c \
    src/core/lib/iomgr/polling_entity.c \
    src/core/lib/iomgr/pollset_set_uv.c \
    src/core/lib/iomgr/pollset_set_windows.c \
    src/core/lib/iomgr/pollset_uv.c \
    src/core/lib/iomgr/pollset_windows.c \
    src/core/lib/iomgr/resolve_address_posix.c \
    src/core/lib/iomgr/resolve_address_uv.c \
    src/core/lib/iomgr/resolve_address_windows.c \
    src/core/lib/iomgr/resource_quota.c \
    src/core/lib/iomgr/sockaddr_utils.c \
    src/core/lib/iomgr/socket_utils_common_posix.c \
    src/core/lib/iomgr/socket_utils_linux.c \
    src/core/lib/iomgr/socket_utils_posix.c \
    src/core/lib/iomgr/socket_utils_uv.c \
    src/core/lib/iomgr/socket_utils_windows.c \
    src/core/lib/iomgr/socket_windows.c \
    src/core/lib/iomgr/tcp_client_posix.c \
    src/core/lib/iomgr/tcp_client_uv.c \
    src/core/lib/iomgr/tcp_client_windows.c \
    src/core/lib/iomgr/tcp_posix.c \
    src/core/lib/iomgr/tcp_server_posix.c \
    src/core/lib/iomgr/tcp_server_uv.c \
    src/core/lib/iomgr/tcp_server_windows.c \
    src/core/lib/iomgr/tcp_uv.c \
    src/core/lib/iomgr/tcp_windows.c \
    src/core/lib/iomgr/time_averaged_stats.c \
    src/core/lib/iomgr/timer_generic.c \
    src/core/lib/iomgr/timer_heap.c \
    src/core/lib/iomgr/timer_uv.c \
    src/core/lib/iomgr/udp_server.c \
    src/core/lib/iomgr/unix_sockets_posix.c \
    src/core/lib/iomgr/unix_sockets_posix_noop.c \
    src/core/lib/iomgr/wakeup_fd_cv.c \
    src/core/lib/iomgr/wakeup_fd_eventfd.c \
    src/core/lib/iomgr/wakeup_fd_nospecial.c \
    src/core/lib/iomgr/wakeup_fd_pipe.c \
    src/core/lib/iomgr/wakeup_fd_posix.c \
    src/core/lib/iomgr/workqueue_uv.c \
    src/core/lib/iomgr/workqueue_windows.c \
    src/core/lib/json/json.c \
    src/core/lib/json/json_reader.c \
    src/core/lib/json/json_string.c \
    src/core/lib/json/json_writer.c \
    src/core/lib/surface/alarm.c \
    src/core/lib/surface/api_trace.c \
    src/core/lib/surface/byte_buffer.c \
    src/core/lib/surface/byte_buffer_reader.c \
    src/core/lib/surface/call.c \
    src/core/lib/surface/call_details.c \
    src/core/lib/surface/call_log_batch.c \
    src/core/lib/surface/channel.c \
    src/core/lib/surface/channel_init.c \
    src/core/lib/surface/channel_ping.c \
    src/core/lib/surface/channel_stack_type.c \
    src/core/lib/surface/completion_queue.c \
    src/core/lib/surface/event_string.c \
    src/core/lib/surface/lame_client.c \
    src/core/lib/surface/metadata_array.c \
    src/core/lib/surface/server.c \
    src/core/lib/surface/validate_metadata.c \
    src/core/lib/surface/version.c \
    src/core/lib/transport/byte_stream.c \
    src/core/lib/transport/connectivity_state.c \
    src/core/lib/transport/mdstr_hash_table.c \
    src/core/lib/transport/metadata.c \
    src/core/lib/transport/metadata_batch.c \
    src/core/lib/transport/method_config.c \
    src/core/lib/transport/pid_controller.c \
    src/core/lib/transport/static_metadata.c \
    src/core/lib/transport/timeout_encoding.c \
    src/core/lib/transport/transport.c \
    src/core/lib/transport/transport_op_string.c \
    src/core/ext/transport/chttp2/server/secure/server_secure_chttp2.c \
    src/core/ext/transport/chttp2/transport/bin_decoder.c \
    src/core/ext/transport/chttp2/transport/bin_encoder.c \
    src/core/ext/transport/chttp2/transport/chttp2_plugin.c \
    src/core/ext/transport/chttp2/transport/chttp2_transport.c \
    src/core/ext/transport/chttp2/transport/frame_data.c \
    src/core/ext/transport/chttp2/transport/frame_goaway.c \
    src/core/ext/transport/chttp2/transport/frame_ping.c \
    src/core/ext/transport/chttp2/transport/frame_rst_stream.c \
    src/core/ext/transport/chttp2/transport/frame_settings.c \
    src/core/ext/transport/chttp2/transport/frame_window_update.c \
    src/core/ext/transport/chttp2/transport/hpack_encoder.c \
    src/core/ext/transport/chttp2/transport/hpack_parser.c \
    src/core/ext/transport/chttp2/transport/hpack_table.c \
    src/core/ext/transport/chttp2/transport/huffsyms.c \
    src/core/ext/transport/chttp2/transport/incoming_metadata.c \
    src/core/ext/transport/chttp2/transport/parsing.c \
    src/core/ext/transport/chttp2/transport/status_conversion.c \
    src/core/ext/transport/chttp2/transport/stream_lists.c \
    src/core/ext/transport/chttp2/transport/stream_map.c \
    src/core/ext/transport/chttp2/transport/varint.c \
    src/core/ext/transport/chttp2/transport/writing.c \
    src/core/ext/transport/chttp2/alpn/alpn.c \
    src/core/lib/http/httpcli_security_connector.c \
    src/core/lib/security/context/security_context.c \
    src/core/lib/security/credentials/composite/composite_credentials.c \
    src/core/lib/security/credentials/credentials.c \
    src/core/lib/security/credentials/credentials_metadata.c \
    src/core/lib/security/credentials/fake/fake_credentials.c \
    src/core/lib/security/credentials/google_default/credentials_generic.c \
    src/core/lib/security/credentials/google_default/google_default_credentials.c \
    src/core/lib/security/credentials/iam/iam_credentials.c \
    src/core/lib/security/credentials/jwt/json_token.c \
    src/core/lib/security/credentials/jwt/jwt_credentials.c \
    src/core/lib/security/credentials/jwt/jwt_verifier.c \
    src/core/lib/security/credentials/oauth2/oauth2_credentials.c \
    src/core/lib/security/credentials/plugin/plugin_credentials.c \
    src/core/lib/security/credentials/ssl/ssl_credentials.c \
    src/core/lib/security/transport/client_auth_filter.c \
    src/core/lib/security/transport/handshake.c \
    src/core/lib/security/transport/secure_endpoint.c \
    src/core/lib/security/transport/security_connector.c \
    src/core/lib/security/transport/server_auth_filter.c \
    src/core/lib/security/transport/tsi_error.c \
    src/core/lib/security/util/b64.c \
    src/core/lib/security/util/json_util.c \
    src/core/lib/surface/init_secure.c \
    src/core/lib/tsi/fake_transport_security.c \
    src/core/lib/tsi/ssl_transport_security.c \
    src/core/lib/tsi/transport_security.c \
    src/core/ext/transport/chttp2/client/secure/secure_channel_create.c \
    src/core/ext/client_channel/channel_connectivity.c \
    src/core/ext/client_channel/client_channel.c \
    src/core/ext/client_channel/client_channel_factory.c \
    src/core/ext/client_channel/client_channel_plugin.c \
    src/core/ext/client_channel/connector.c \
    src/core/ext/client_channel/default_initial_connect_string.c \
    src/core/ext/client_channel/http_connect_handshaker.c \
    src/core/ext/client_channel/initial_connect_string.c \
    src/core/ext/client_channel/lb_policy.c \
    src/core/ext/client_channel/lb_policy_factory.c \
    src/core/ext/client_channel/lb_policy_registry.c \
    src/core/ext/client_channel/parse_address.c \
    src/core/ext/client_channel/resolver.c \
    src/core/ext/client_channel/resolver_factory.c \
    src/core/ext/client_channel/resolver_registry.c \
    src/core/ext/client_channel/subchannel.c \
    src/core/ext/client_channel/subchannel_index.c \
    src/core/ext/client_channel/uri_parser.c \
    src/core/ext/transport/chttp2/server/insecure/server_chttp2.c \
    src/core/ext/transport/chttp2/server/insecure/server_chttp2_posix.c \
    src/core/ext/transport/chttp2/client/insecure/channel_create.c \
    src/core/ext/transport/chttp2/client/insecure/channel_create_posix.c \
    src/core/ext/lb_policy/grpclb/grpclb.c \
    src/core/ext/lb_policy/grpclb/load_balancer_api.c \
    src/core/ext/lb_policy/grpclb/proto/grpc/lb/v1/load_balancer.pb.c \
    third_party/nanopb/pb_common.c \
    third_party/nanopb/pb_decode.c \
    third_party/nanopb/pb_encode.c \
    src/core/ext/lb_policy/pick_first/pick_first.c \
    src/core/ext/lb_policy/round_robin/round_robin.c \
    src/core/ext/resolver/dns/native/dns_resolver.c \
    src/core/ext/resolver/sockaddr/sockaddr_resolver.c \
    src/core/ext/load_reporting/load_reporting.c \
    src/core/ext/load_reporting/load_reporting_filter.c \
    src/core/ext/census/base_resources.c \
    src/core/ext/census/context.c \
    src/core/ext/census/gen/census.pb.c \
    src/core/ext/census/gen/trace_context.pb.c \
    src/core/ext/census/grpc_context.c \
    src/core/ext/census/grpc_filter.c \
    src/core/ext/census/grpc_plugin.c \
    src/core/ext/census/initialize.c \
    src/core/ext/census/mlog.c \
    src/core/ext/census/operation.c \
    src/core/ext/census/placeholders.c \
    src/core/ext/census/resource.c \
    src/core/ext/census/trace_context.c \
    src/core/ext/census/tracing.c \
    src/core/plugin_registry/grpc_plugin_registry.c \
    , $ext_shared, , -Wall -Werror \
    -Wno-parentheses-equality -Wno-unused-value -std=c11 \
    -fvisibility=hidden -DOPENSSL_NO_ASM -D_GNU_SOURCE -DWIN32_LEAN_AND_MEAN \
    -D_HAS_EXCEPTIONS=0 -DNOMINMAX)

  PHP_ADD_BUILD_DIR($ext_builddir/src/php/ext/grpc)

  PHP_ADD_BUILD_DIR($ext_builddir/src/core/ext/census)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/ext/census/gen)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/ext/client_channel)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/ext/lb_policy/grpclb)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/ext/lb_policy/grpclb/proto/grpc/lb/v1)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/ext/lb_policy/pick_first)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/ext/lb_policy/round_robin)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/ext/load_reporting)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/ext/resolver/dns/native)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/ext/resolver/sockaddr)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/ext/transport/chttp2/alpn)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/ext/transport/chttp2/client/insecure)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/ext/transport/chttp2/client/secure)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/ext/transport/chttp2/server/insecure)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/ext/transport/chttp2/server/secure)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/ext/transport/chttp2/transport)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/lib/channel)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/lib/compression)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/lib/debug)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/lib/http)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/lib/iomgr)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/lib/json)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/lib/profiling)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/lib/security/context)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/lib/security/credentials)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/lib/security/credentials/composite)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/lib/security/credentials/fake)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/lib/security/credentials/google_default)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/lib/security/credentials/iam)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/lib/security/credentials/jwt)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/lib/security/credentials/oauth2)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/lib/security/credentials/plugin)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/lib/security/credentials/ssl)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/lib/security/transport)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/lib/security/util)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/lib/support)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/lib/surface)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/lib/transport)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/lib/tsi)
  PHP_ADD_BUILD_DIR($ext_builddir/src/core/plugin_registry)
  PHP_ADD_BUILD_DIR($ext_builddir/third_party/nanopb)
fi
